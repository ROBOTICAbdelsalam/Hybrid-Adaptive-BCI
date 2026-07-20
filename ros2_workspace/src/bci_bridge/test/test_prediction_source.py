"""Unit tests for the AI-output reader / gesture mapper.

Pure Python, so runnable on the macOS dev host. Where possible these run
against the REAL artefacts the pipeline produced, proving the bridge consumes
the existing outputs unmodified.
"""

import csv
import os

from bci_bridge import prediction_source as ps

# Repo root = four levels up: test/ -> bci_bridge -> src -> ros2_workspace -> repo
REPO_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "..")
)
REAL_PREDICTIONS = os.path.join(
    REPO_ROOT, "realtime", "results", "realtime_predictions.csv")
REAL_THRESHOLD = os.path.join(
    REPO_ROOT, "adaptive_ai", "adaptive_threshold.csv")


def _write_csv(path, rows, fieldnames):
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


# -- mapping / gating logic -------------------------------------------------

def test_high_confidence_maps_to_gesture():
    gesture, reason = ps.to_gesture(
        ps.Prediction(prediction=1, confidence=0.9), threshold=0.75)
    assert gesture == 1
    assert reason == "accepted"


def test_below_threshold_is_no_op():
    gesture, reason = ps.to_gesture(
        ps.Prediction(prediction=1, confidence=0.5), threshold=0.75)
    assert gesture is None
    assert "below threshold" in reason


def test_unmapped_class_is_no_op():
    gesture, reason = ps.to_gesture(
        ps.Prediction(prediction=7, confidence=0.99), threshold=0.75)
    assert gesture is None
    assert "unmapped" in reason


def test_default_mapping_covers_model_classes():
    assert set(ps.DEFAULT_CLASS_TO_GESTURE) == {0, 1, 2}


# -- robustness -------------------------------------------------------------

def test_load_threshold_falls_back_when_missing(tmp_path):
    missing = str(tmp_path / "nope.csv")
    assert ps.load_threshold(missing, default=0.8) == 0.8


def test_read_and_map_roundtrip(tmp_path):
    csv_path = str(tmp_path / "preds.csv")
    _write_csv(
        csv_path,
        [{"Prediction": 2, "Confidence": 0.95},
         {"Prediction": 0, "Confidence": 0.10}],
        ["Prediction", "Confidence"],
    )
    preds = ps.read_predictions(csv_path)
    assert len(preds) == 2
    assert ps.to_gesture(preds[0], 0.75)[0] == 2   # accepted
    assert ps.to_gesture(preds[1], 0.75)[0] is None  # gated out


# -- against the real pipeline output ---------------------------------------

def test_reads_real_pipeline_predictions_if_present():
    if not os.path.exists(REAL_PREDICTIONS):
        return  # artefact not generated in this checkout; skip silently
    preds = ps.read_predictions(REAL_PREDICTIONS)
    assert preds, "expected at least one prediction row"
    for p in preds:
        assert isinstance(p.prediction, int)
        assert 0.0 <= p.confidence <= 1.0


def test_reads_real_adaptive_threshold_if_present():
    if not os.path.exists(REAL_THRESHOLD):
        return
    thr = ps.load_threshold(REAL_THRESHOLD)
    assert 0.0 < thr <= 1.0
