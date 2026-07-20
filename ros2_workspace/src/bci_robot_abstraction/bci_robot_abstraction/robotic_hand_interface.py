"""Robotic hand implementation of :class:`RobotInterface`.

The hand is the primary demonstration platform. It supports the full gesture
vocabulary and maps each gesture to a named pose plus per-joint targets. The
named poses match the states declared for MoveIt2 (added in a later phase),
and the joint targets drive the Gazebo controllers.

Pure Python (no ROS2), so the full gesture->pose mapping is unit-testable.
"""

from __future__ import annotations

from . import gesture_library
from .robot_interface import GestureResult, RobotInterface

# Five actuated finger joints (thumb, index, middle, ring, little).
# Values are normalised flexion in [0.0 = fully open, 1.0 = fully closed].
FINGER_JOINTS = ("thumb_joint", "index_joint", "middle_joint",
                 "ring_joint", "little_joint")


def _pose(thumb: float, index: float, middle: float,
          ring: float, little: float) -> dict[str, float]:
    return dict(zip(FINGER_JOINTS, (thumb, index, middle, ring, little)))


# Gesture id -> (named_pose, joint targets). Named poses mirror the MoveIt SRDF.
_HAND_POSES: dict[int, tuple[str, dict[str, float]]] = {
    gesture_library.id_of("REST"):
        ("rest", _pose(0.2, 0.2, 0.2, 0.2, 0.2)),
    gesture_library.id_of("OPEN_HAND"):
        ("open_hand", _pose(0.0, 0.0, 0.0, 0.0, 0.0)),
    gesture_library.id_of("CLOSE_HAND"):
        ("close_hand", _pose(1.0, 1.0, 1.0, 1.0, 1.0)),
    gesture_library.id_of("PINCH_GRIP"):
        ("pinch_grip", _pose(1.0, 1.0, 0.0, 0.0, 0.0)),
    gesture_library.id_of("POWER_GRIP"):
        ("power_grip", _pose(0.9, 0.9, 0.9, 0.9, 0.9)),
    gesture_library.id_of("POINT"):
        ("point", _pose(1.0, 0.0, 1.0, 1.0, 1.0)),
}


class RoboticHand(RobotInterface):
    """Five-finger robotic hand supporting all six BCI gestures."""

    def __init__(self, robot_id: str = "robotic_hand") -> None:
        self._id = robot_id

    @property
    def name(self) -> str:
        return self._id

    def supported_gestures(self) -> set[int]:
        return set(_HAND_POSES.keys())

    def _plan_gesture(self, gesture: int) -> GestureResult:
        pose_name, targets = _HAND_POSES[gesture]
        return GestureResult(
            accepted=True,
            message=f"{self._id}: {pose_name}",
            named_pose=pose_name,
            joint_targets=dict(targets),
        )
