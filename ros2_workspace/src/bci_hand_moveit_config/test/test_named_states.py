"""Cross-package consistency test for the six named gesture states.

Proves that every SRDF group_state equals the robot abstraction's normalised
gesture pose multiplied by the URDF finger-joint limit. This binds three
packages to a single source of truth so the gestures cannot drift apart:

    abstraction (normalised)  x  URDF limit (rad)  ==  SRDF named state (rad)

Uses xacro (available on ROS2 hosts and via pip on the dev host) and the
standard library only.
"""

import os
import sys
import xml.etree.ElementTree as ET

import xacro

HERE = os.path.dirname(__file__)
SRC = os.path.abspath(os.path.join(HERE, "..", ".."))
SRDF = os.path.join(SRC, "bci_hand_moveit_config", "config", "bci_hand.srdf")
XACRO = os.path.join(SRC, "bci_hand_description", "urdf", "bci_hand.urdf.xacro")

# Import the abstraction's pure-Python core directly from source.
sys.path.insert(0, os.path.join(SRC, "bci_robot_abstraction"))
from bci_robot_abstraction.robotic_hand_interface import (  # noqa: E402
    _HAND_POSES, FINGER_JOINTS,
)

TOL = 1e-6


def _urdf_max_flexion():
    doc = xacro.process_file(XACRO, mappings={"controllers_config": "/tmp/x.yaml"})
    root = ET.fromstring(doc.toprettyxml(indent="  "))
    uppers = {
        float(j.find("limit").get("upper"))
        for j in root.findall("joint") if j.get("type") == "revolute"
    }
    assert len(uppers) == 1, f"finger joints have differing limits: {uppers}"
    return uppers.pop()


def _srdf_named_states():
    root = ET.parse(SRDF).getroot()
    states = {}
    for gs in root.findall("group_state"):
        states[gs.get("name")] = {
            j.get("name"): float(j.get("value"))
            for j in gs.findall("joint")
        }
    return states


def test_srdf_has_all_six_gestures():
    states = _srdf_named_states()
    abstraction_names = {name for name, _ in _HAND_POSES.values()}
    assert set(states) == abstraction_names
    assert len(states) == 6


def test_named_states_match_abstraction_times_urdf_limit():
    max_flex = _urdf_max_flexion()
    srdf = _srdf_named_states()

    # Map joint index -> joint name (abstraction pose values are ordered).
    for _gid, (pose_name, targets) in _HAND_POSES.items():
        expected = {j: targets[j] * max_flex for j in FINGER_JOINTS}
        actual = srdf[pose_name]
        assert set(actual) == set(FINGER_JOINTS), pose_name
        for joint in FINGER_JOINTS:
            assert abs(actual[joint] - expected[joint]) < TOL, (
                f"{pose_name}.{joint}: SRDF={actual[joint]} "
                f"expected={expected[joint]} (norm {targets[joint]} x {max_flex})"
            )


def test_planning_group_covers_all_finger_joints():
    root = ET.parse(SRDF).getroot()
    group = root.find("group")
    assert group.get("name") == "hand"
    joints = {j.get("name") for j in group.findall("joint")}
    assert joints == set(FINGER_JOINTS)
