import os
import shutil
import numpy as np
import matplotlib.pyplot as plt
import mne
from mne.datasets import eegbci

print("=" * 60)
print("Lab 08.5 - Epoch Quality Check")
print("=" * 60)

# --------------------------------------------------
# Create folders
# --------------------------------------------------
os.makedirs("results", exist_ok=True)
os.makedirs("figures", exist_ok=True)
os.makedirs("docs/images", exist_ok=True)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------
subject = 1
runs = [4]

files = eegbci.load_data(subject, runs)

raw = mne.io.read_raw_edf(files[0], preload=True)

events, event_id = mne.events_from_annotations(raw)

epochs = mne.Epochs(
    raw,
    events,
    event_id=event_id,
    tmin=-0.2,
    tmax=0.8,
    baseline=(-0.2, 0),
    preload=True
)

data = epochs.get_data()

print(f"\nValid Epochs : {len(epochs)}")
print(f"Epoch Shape  : {data.shape}")

# --------------------------------------------------
# Quality Checks
# --------------------------------------------------
has_nan = np.isnan(data).any()
has_inf = np.isinf(data).any()

print(f"Contains NaN : {has_nan}")
print(f"Contains Inf : {has_inf}")

# --------------------------------------------------
# Save Report
# --------------------------------------------------
with open(
    "results/lab08_05_epoch_quality_check_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab 08.5 - Epoch Quality Check\n")
    report.write("=" * 50 + "\n\n")

    report.write(f"Valid Epochs : {len(epochs)}\n")
    report.write(f"Epoch Shape  : {data.shape}\n\n")

    report.write(f"Contains NaN : {has_nan}\n")
    report.write(f"Contains Inf : {has_inf}\n")

print("Report Saved.")

# --------------------------------------------------
# Quality Figure
# --------------------------------------------------
epoch_std = data.std(axis=(1, 2))

plt.figure(figsize=(8,4))
plt.plot(epoch_std, marker='o')
plt.title("Epoch Quality Check")
plt.xlabel("Epoch Index")
plt.ylabel("Standard Deviation")
plt.grid(True)

plt.savefig(
    "figures/lab08_epoch_quality.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Figure Saved.")

# --------------------------------------------------
# Copy Figure
# --------------------------------------------------
shutil.copy(
    "figures/lab08_epoch_quality.png",
    "docs/images/lab08_epoch_quality.png"
)

print("Documentation Figure Saved.")

print("\nLab08.5 Finished Successfully.")
