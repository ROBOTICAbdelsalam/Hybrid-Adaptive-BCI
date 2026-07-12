import os
import joblib
import numpy as np
import mne
from mne.datasets import eegbci
from mne.decoding import CSP

print("=" * 60)
print("Lab10.1 - CSP Theory")
print("=" * 60)

os.makedirs("csp", exist_ok=True)
os.makedirs("results", exist_ok=True)

subject = 1
runs = [4]

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

files = eegbci.load_data(subject, runs)

raw = mne.io.read_raw_edf(
    files[0],
    preload=True,
    verbose=False
)

raw.rename_channels(lambda x: x.strip("."))

events, event_id = mne.events_from_annotations(raw)

picks = mne.pick_types(
    raw.info,
    eeg=True,
    exclude="bads"
)

epochs = mne.Epochs(
    raw,
    events,
    event_id=event_id,
    tmin=0.0,
    tmax=1.0,
    baseline=None,
    preload=True,
    picks=picks,
    verbose=False
)

X = epochs.get_data()
y = epochs.events[:, 2]

print("Epochs :", X.shape)
print("Labels :", np.unique(y))

# --------------------------------------------------
# Train CSP
# --------------------------------------------------

csp = CSP(
    n_components=4,
    reg=None,
    log=True,
    norm_trace=False
)

csp.fit(X, y)

joblib.dump(
    csp,
    "csp/csp_model.pkl"
)

print("CSP model saved.")

# --------------------------------------------------
# Report
# --------------------------------------------------

with open(
    "results/lab10_01_csp_theory_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab10.1 - CSP Theory\n")
    report.write("=" * 50 + "\n\n")

    report.write(f"Epoch Shape : {X.shape}\n")
    report.write(f"Classes     : {list(np.unique(y))}\n")
    report.write(f"CSP Components : {csp.n_components}\n")

print("Report Saved.")
print("\nLab10.1 Finished Successfully.")
