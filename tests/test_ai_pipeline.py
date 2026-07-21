"""Scientific-invariant validation for the AI pipeline (Labs 01-14).

These tests do not retrain anything. They load the committed artefacts and assert
the invariants that make the pipeline correct and reproducible:

  * the "processed" epochs are actually filtered (fix A4),
  * the train-only CSP model transforms epochs to 4 features (fix A2),
  * the train/test split is disjoint — no leakage at the feature level (A2/A3),
  * features contain no NaN/Inf,
  * the deployed deep-learning model has the expected I/O and yields probabilities.

Run: ``pytest tests/ -q`` (needs the AI dependencies from requirements.txt).
"""

import os

import numpy as np
import pandas as pd
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _p(*parts):
    return os.path.join(ROOT, *parts)


# ---------------------------------------------------------------------------
# A4 — preprocessing actually happened
# ---------------------------------------------------------------------------

def test_processed_epochs_are_band_pass_filtered():
    mne = pytest.importorskip("mne")
    epo = _p("processed_data", "subject01_run04-epo.fif")
    assert os.path.exists(epo), "processed epochs missing"
    ep = mne.read_epochs(epo, preload=True, verbose=False)
    assert abs(ep.info["highpass"] - 1.0) < 1e-6, "expected 1 Hz high-pass (A4)"
    assert abs(ep.info["lowpass"] - 40.0) < 1e-6, "expected 40 Hz low-pass (A4)"


# ---------------------------------------------------------------------------
# A2 — leakage-free CSP
# ---------------------------------------------------------------------------

def test_train_only_csp_model_transforms_to_four_features():
    mne = pytest.importorskip("mne")
    joblib = pytest.importorskip("joblib")
    csp = joblib.load(_p("csp", "csp_model_train.pkl"))
    ep = mne.read_epochs(
        _p("processed_data", "subject01_run04-epo.fif"),
        preload=True, verbose=False)
    feats = csp.transform(ep.get_data(copy=True)[:6])
    assert feats.shape == (6, 4)
    assert np.isfinite(feats).all()


# ---------------------------------------------------------------------------
# Split integrity — shapes, labels, no leakage
# ---------------------------------------------------------------------------

def test_ml_split_shapes_and_labels():
    xtr = pd.read_csv(_p("ml_data", "X_train.csv"))
    xte = pd.read_csv(_p("ml_data", "X_test.csv"))
    ytr = pd.read_csv(_p("ml_data", "y_train.csv")).squeeze("columns")
    yte = pd.read_csv(_p("ml_data", "y_test.csv")).squeeze("columns")
    assert xtr.shape == (23, 4) and xte.shape == (6, 4)
    assert list(xtr.columns) == ["CSP_1", "CSP_2", "CSP_3", "CSP_4"]
    assert set(ytr) | set(yte) <= {1, 2, 3}
    assert len(ytr) == 23 and len(yte) == 6


def test_train_and_test_features_are_disjoint():
    """No test row may appear in the training set (feature-level leakage check)."""
    xtr = pd.read_csv(_p("ml_data", "X_train.csv")).round(6)
    xte = pd.read_csv(_p("ml_data", "X_test.csv")).round(6)
    train_rows = {tuple(r) for r in xtr.to_numpy()}
    overlap = [tuple(r) for r in xte.to_numpy() if tuple(r) in train_rows]
    assert not overlap, f"{len(overlap)} test rows leaked into train"


def test_features_have_no_nan_or_inf():
    for name in ("X_train.csv", "X_test.csv"):
        arr = pd.read_csv(_p("ml_data", name)).to_numpy()
        assert np.isfinite(arr).all(), f"{name} contains NaN/Inf"


def test_dl_data_matches_ml_data():
    xtr = np.load(_p("dl_data", "X_train.npy"))
    xte = np.load(_p("dl_data", "X_test.npy"))
    assert xtr.shape == (23, 4, 1)
    assert xte.shape == (6, 4, 1)


# ---------------------------------------------------------------------------
# Deployed deep-learning model
# ---------------------------------------------------------------------------

def test_deployed_model_io_and_probabilities():
    tf = pytest.importorskip("tensorflow")
    model = tf.keras.models.load_model(
        _p("models", "final_deep_learning_model.keras"), compile=False)
    assert model.input_shape == (None, 4, 1)
    assert model.output_shape == (None, 3)
    x = np.load(_p("dl_data", "X_test.npy")).astype("float32")
    probs = model.predict(x, verbose=0)
    assert probs.shape == (6, 3)
    # softmax outputs: each row sums to 1
    assert np.allclose(probs.sum(axis=1), 1.0, atol=1e-4)
