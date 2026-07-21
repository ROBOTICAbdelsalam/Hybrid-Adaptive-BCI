"""Structural verification of the robotic hand URDF/Xacro.

Expands the xacro and validates the resulting URDF with the standard library
only (plus xacro, which is available both on ROS2 hosts and via pip on the dev
machine). No ROS runtime or Gazebo required, so it runs anywhere.
"""

import os
import xml.etree.ElementTree as ET

import xacro

HERE = os.path.dirname(__file__)
XACRO = os.path.abspath(os.path.join(HERE, "..", "urdf", "bci_hand.urdf.xacro"))

FINGER_JOINTS = {"thumb_joint", "index_joint", "middle_joint",
                 "ring_joint", "little_joint"}


def _urdf_root():
    doc = xacro.process_file(XACRO, mappings={"controllers_config": "/tmp/x.yaml"})
    return ET.fromstring(doc.toprettyxml(indent="  "))


def test_xacro_expands_and_is_valid_xml():
    root = _urdf_root()
    assert root.tag == "robot"
    assert root.get("name") == "bci_hand"


def test_five_actuated_finger_joints_with_correct_limits():
    root = _urdf_root()
    revolute = {j.get("name"): j for j in root.findall("joint")
                if j.get("type") == "revolute"}
    assert set(revolute) == FINGER_JOINTS
    for name, joint in revolute.items():
        limit = joint.find("limit")
        assert limit is not None, f"{name} has no <limit>"
        assert float(limit.get("lower")) == 0.0
        assert abs(float(limit.get("upper")) - 1.4) < 1e-9


def test_every_joint_references_existing_links():
    root = _urdf_root()
    links = {link.get("name") for link in root.findall("link")}
    for joint in root.findall("joint"):
        parent = joint.find("parent").get("link")
        child = joint.find("child").get("link")
        assert parent in links, f"missing parent link {parent}"
        assert child in links, f"missing child link {child}"


def test_kinematic_tree_is_connected_and_acyclic():
    root = _urdf_root()
    links = {link.get("name") for link in root.findall("link")}
    children = [j.find("child").get("link") for j in root.findall("joint")]
    # Exactly one root link (never a child) -> single connected tree.
    roots = links - set(children)
    assert roots == {"world"}, f"expected single root 'world', got {roots}"
    # No link is the child of two joints (no cycles / re-parenting).
    assert len(children) == len(set(children)), "a link has multiple parents"


def test_ros2_control_declares_all_finger_joints():
    root = _urdf_root()
    r2c = root.find("ros2_control")
    assert r2c is not None, "missing <ros2_control> block"
    ctrl_joints = {j.get("name") for j in r2c.findall("joint")}
    assert ctrl_joints == FINGER_JOINTS


def test_gazebo_ros2_control_plugin_present():
    root = _urdf_root()
    plugins = [p.get("filename") for g in root.findall("gazebo")
               for p in g.findall("plugin")]
    assert any("gz_ros2_control" in (p or "") for p in plugins)
