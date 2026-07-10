from mne.datasets import eegbci
import mne
from mne.preprocessing import ICA

print("=" * 50)
print("Lab 07 - ICA Model")
print("=" * 50)

# -----------------------------------
# Load Dataset
# -----------------------------------

subject = 1
runs = [4]

files = eegbci.load_data(subject, runs)

raw = mne.io.read_raw_edf(
    files[0],
    preload=True
)

print("\nDataset Loaded Successfully")

# -----------------------------------
# Filtering
# -----------------------------------

print("Applying Band-pass Filter (1-40 Hz)...")

raw.filter(
    l_freq=1,
    h_freq=40
)

print("Filtering Completed")

# -----------------------------------
# ICA
# -----------------------------------

print("\nCreating ICA Model...")

ica = ICA(
    n_components=20,
    random_state=42,
    method="fastica"
)

print("Training ICA...")

ica.fit(raw)

print("\nICA Training Completed Successfully")