"""Lightweight metrics helpers (pure Python, no ROS imports, unit-tested).

Used by the ROS2 nodes to report command latency without pulling any ROS
dependency into the tested core.
"""

from __future__ import annotations


def latency_ms(
    sent_sec: int, sent_nanosec: int, recv_sec: int, recv_nanosec: int
) -> float:
    """Milliseconds between two ROS time stamps (``builtin_interfaces/Time``).

    Clamped at 0 so clock skew never reports a negative latency.
    """
    sent = sent_sec + sent_nanosec * 1e-9
    recv = recv_sec + recv_nanosec * 1e-9
    return max(0.0, (recv - sent) * 1000.0)


class LatencyStats:
    """Running min/mean/max of a latency stream (constant memory)."""

    def __init__(self) -> None:
        self.count = 0
        self.total = 0.0
        self.min = float("inf")
        self.max = 0.0

    def update(self, value_ms: float) -> None:
        self.count += 1
        self.total += value_ms
        self.min = min(self.min, value_ms)
        self.max = max(self.max, value_ms)

    @property
    def mean(self) -> float:
        return self.total / self.count if self.count else 0.0

    def summary(self) -> str:
        if not self.count:
            return "latency: no samples"
        return (f"latency ms: mean={self.mean:.1f} "
                f"min={self.min:.1f} max={self.max:.1f} n={self.count}")
