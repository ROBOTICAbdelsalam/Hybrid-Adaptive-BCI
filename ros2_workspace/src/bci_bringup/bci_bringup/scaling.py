"""Pure scaling helpers for the hand adapter (no ROS imports, unit-tested)."""

from __future__ import annotations


def scale_to_radians(
    normalized: list[float], max_flexion: float
) -> list[float]:
    """Scale normalised flexion [0,1] to joint radians [0, max_flexion].

    Each value is clamped to [0, 1] first, so an out-of-range input can never
    command a joint past its limit.
    """
    return [max(0.0, min(1.0, v)) * max_flexion for v in normalized]
