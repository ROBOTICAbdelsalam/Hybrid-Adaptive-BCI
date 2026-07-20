"""Single source of truth for the robot-independent gesture vocabulary.

The integer ids here MUST stay in sync with the constants declared in
``bci_interfaces/msg/BCICommand.msg``. Keeping the mapping in plain Python
(no ROS2 imports) lets every layer - bridge, abstraction, tests - share one
definition and lets the core logic be tested without a ROS2 installation.
"""

from __future__ import annotations

# Gesture id -> canonical name. Order/values match BCICommand.msg constants.
GESTURES: dict[int, str] = {
    0: "REST",
    1: "OPEN_HAND",
    2: "CLOSE_HAND",
    3: "PINCH_GRIP",
    4: "POWER_GRIP",
    5: "POINT",
}

NAME_TO_ID: dict[str, int] = {name: gid for gid, name in GESTURES.items()}


def is_valid(gesture: int) -> bool:
    """Return True if ``gesture`` is a known gesture id."""
    return gesture in GESTURES


def name_of(gesture: int) -> str:
    """Return the canonical name for a gesture id.

    Raises:
        KeyError: if the gesture id is unknown.
    """
    return GESTURES[gesture]


def id_of(name: str) -> int:
    """Return the gesture id for a canonical name (case-insensitive).

    Raises:
        KeyError: if the name is unknown.
    """
    return NAME_TO_ID[name.strip().upper()]
