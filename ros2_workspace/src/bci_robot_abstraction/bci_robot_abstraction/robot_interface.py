"""Robot-independent interface every robot must implement.

This is the seam that keeps the EEG/AI pipeline decoupled from the hardware.
The bridge and robot node speak only in terms of ``RobotInterface`` and
semantic gestures, so a robotic hand, a UR5e or a Franka Panda are all added
by writing a new subclass - never by touching the AI code.

Deliberately free of ROS2 imports so it can be unit-tested anywhere.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from . import gesture_library


@dataclass
class GestureResult:
    """Outcome of asking a robot to perform a gesture.

    ``joint_targets`` and ``named_pose`` describe HOW the robot will realise
    the gesture; the ROS2 layer turns them into controller/MoveIt commands.
    """

    accepted: bool
    message: str
    named_pose: str | None = None
    joint_targets: dict[str, float] = field(default_factory=dict)


class RobotInterface(ABC):
    """Abstract contract shared by all robots controlled via BCI."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Stable identifier, e.g. ``"robotic_hand"``."""

    @abstractmethod
    def supported_gestures(self) -> set[int]:
        """Set of gesture ids this robot can perform."""

    @abstractmethod
    def _plan_gesture(self, gesture: int) -> GestureResult:
        """Robot-specific realisation of a (already validated) gesture."""

    def execute_gesture(self, gesture: int, confidence: float) -> GestureResult:
        """Validate then realise a gesture. Common to every robot.

        Rejection is a normal, safe outcome - unknown or unsupported gestures
        never reach robot-specific code.
        """
        if not gesture_library.is_valid(gesture):
            return GestureResult(
                accepted=False,
                message=f"Unknown gesture id {gesture}",
            )
        if gesture not in self.supported_gestures():
            return GestureResult(
                accepted=False,
                message=(
                    f"{self.name} does not support gesture "
                    f"'{gesture_library.name_of(gesture)}'"
                ),
            )
        result = self._plan_gesture(gesture)
        return result
