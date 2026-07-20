"""Unit tests for the robot-independent abstraction core.

No ROS2 dependency, so these run on any Python (including the macOS dev host).
"""

from bci_robot_abstraction import gesture_library as gl
from bci_robot_abstraction.robot_interface import RobotInterface, GestureResult
from bci_robot_abstraction.robot_registry import available_robots, create_robot
from bci_robot_abstraction.robotic_hand_interface import (
    RoboticHand, FINGER_JOINTS,
)


# -- gesture library --------------------------------------------------------

def test_gesture_ids_match_msg_contract():
    # Values must match bci_interfaces/msg/BCICommand.msg constants.
    assert gl.GESTURES == {
        0: "REST", 1: "OPEN_HAND", 2: "CLOSE_HAND",
        3: "PINCH_GRIP", 4: "POWER_GRIP", 5: "POINT",
    }


def test_name_id_roundtrip():
    for gid, name in gl.GESTURES.items():
        assert gl.id_of(name) == gid
        assert gl.name_of(gid) == name


def test_id_of_is_case_insensitive():
    assert gl.id_of("open_hand") == gl.id_of("OPEN_HAND")


def test_is_valid():
    assert gl.is_valid(0)
    assert not gl.is_valid(99)


# -- robotic hand -----------------------------------------------------------

def test_hand_supports_all_six_gestures():
    hand = RoboticHand()
    assert hand.supported_gestures() == set(gl.GESTURES)


def test_hand_executes_every_gesture_with_full_joint_targets():
    hand = RoboticHand()
    for gid in gl.GESTURES:
        result = hand.execute_gesture(gid, confidence=0.9)
        assert result.accepted
        assert result.named_pose
        assert set(result.joint_targets) == set(FINGER_JOINTS)
        assert all(0.0 <= v <= 1.0 for v in result.joint_targets.values())


def test_hand_rejects_unknown_gesture():
    result = RoboticHand().execute_gesture(99, confidence=0.9)
    assert not result.accepted
    assert "Unknown" in result.message


def test_open_and_close_are_opposite_extremes():
    hand = RoboticHand()
    opened = hand.execute_gesture(gl.id_of("OPEN_HAND"), 1.0).joint_targets
    closed = hand.execute_gesture(gl.id_of("CLOSE_HAND"), 1.0).joint_targets
    assert all(v == 0.0 for v in opened.values())
    assert all(v == 1.0 for v in closed.values())


# -- registry / robot independence -----------------------------------------

def test_registry_exposes_robotic_hand():
    assert "robotic_hand" in available_robots()
    assert isinstance(create_robot("robotic_hand"), RoboticHand)


def test_registry_rejects_unknown_robot():
    try:
        create_robot("does_not_exist")
    except KeyError:
        pass
    else:  # pragma: no cover
        raise AssertionError("expected KeyError for unknown robot")


def test_unsupported_gesture_is_rejected_generically():
    """A robot that supports nothing must reject via the base class."""

    class NullRobot(RobotInterface):
        @property
        def name(self):
            return "null"

        def supported_gestures(self):
            return set()

        def _plan_gesture(self, gesture):  # pragma: no cover
            raise AssertionError("must not reach robot-specific code")

    result = NullRobot().execute_gesture(gl.id_of("REST"), 1.0)
    assert not result.accepted
    assert isinstance(result, GestureResult)
