"""Read the existing AI pipeline output and turn it into BCI gestures.

Reuses, without modification, the artefacts the EEG/AI pipeline already
produces:
  * realtime/results/realtime_predictions.csv  (Lab 14.4) - class + confidence
  * adaptive_ai/adaptive_threshold.csv          (Lab 13.2) - confidence gate

The AI model emits 3 motor-imagery classes; the robotic hand supports 6
gestures. The class->gesture mapping lives here (and in config), so the AI
code stays untouched while the robot remains ready for the full vocabulary.

Pure Python + stdlib csv (no pandas, no ROS2), so it is unit-testable and
keeps the ROS2 runtime dependency-light.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass

# Default AI class id -> gesture id (BCICommand constants).
# 0,1,2 are the current model's motor-imagery classes.
DEFAULT_CLASS_TO_GESTURE: dict[int, int] = {
    0: 0,  # -> REST
    1: 1,  # -> OPEN_HAND
    2: 2,  # -> CLOSE_HAND
}

DEFAULT_THRESHOLD = 0.75


@dataclass
class Prediction:
    prediction: int
    confidence: float


def read_predictions(csv_path: str) -> list[Prediction]:
    """Load (Prediction, Confidence) rows from the Lab 14.4 output CSV."""
    rows: list[Prediction] = []
    with open(csv_path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            rows.append(
                Prediction(
                    prediction=int(float(row["Prediction"])),
                    confidence=float(row["Confidence"]),
                )
            )
    return rows


def load_threshold(csv_path: str, default: float = DEFAULT_THRESHOLD) -> float:
    """Load the adaptive confidence gate from the Lab 13.2 output.

    Falls back to ``default`` if the file is missing or malformed, so the
    bridge degrades safely rather than crashing.
    """
    try:
        with open(csv_path, newline="", encoding="utf-8") as handle:
            first = next(csv.DictReader(handle))
            return float(first["Adaptive_Threshold"])
    except (OSError, KeyError, StopIteration, ValueError):
        return default


def to_gesture(
    prediction: Prediction,
    threshold: float,
    class_to_gesture: dict[int, int] | None = None,
) -> tuple[int | None, str]:
    """Map one prediction to a gesture id, gated by confidence.

    Returns ``(gesture_id, reason)`` or ``(None, reason)`` when the prediction
    is below threshold or the class is unmapped - both safe no-ops.
    """
    mapping = class_to_gesture or DEFAULT_CLASS_TO_GESTURE

    if prediction.confidence < threshold:
        return None, (
            f"below threshold ({prediction.confidence:.2f} < {threshold:.2f})"
        )
    if prediction.prediction not in mapping:
        return None, f"unmapped class {prediction.prediction}"
    return mapping[prediction.prediction], "accepted"
