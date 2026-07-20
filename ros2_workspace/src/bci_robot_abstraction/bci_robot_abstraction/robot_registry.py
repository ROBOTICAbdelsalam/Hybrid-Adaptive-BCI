"""Registry that maps a robot name to its :class:`RobotInterface` class.

This is the single extension point for new robots. Adding a Franka Panda,
KUKA iiwa or UR5e means writing a ``RobotInterface`` subclass and registering
it here - the bridge, the AI pipeline and the robot node stay untouched.
"""

from __future__ import annotations

from .robot_interface import RobotInterface
from .robotic_hand_interface import RoboticHand

_REGISTRY: dict[str, type[RobotInterface]] = {
    "robotic_hand": RoboticHand,
    # "ur5e": UR5eArm,        # added in a later phase, no AI changes needed
    # "panda": FrankaPanda,
}


def available_robots() -> list[str]:
    """Names of all registered robots."""
    return sorted(_REGISTRY)


def create_robot(name: str) -> RobotInterface:
    """Instantiate a registered robot by name.

    Raises:
        KeyError: if ``name`` is not registered.
    """
    if name not in _REGISTRY:
        raise KeyError(
            f"Unknown robot '{name}'. Available: {available_robots()}"
        )
    return _REGISTRY[name](robot_id=name)
