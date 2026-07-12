import os
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mne
from mne.datasets import eegbci

print("=" * 60)
print("Lab 09.1 - Time Domain Feature Extraction")
print("=" * 60)

# --------------------------------------------------
# Create folders
# --------------------------------------------------
os.makedirs("results", exist_ok=True)
os.makedirs("figures", exist_ok=True)
os.makedirs("features", exist_ok=True)
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

print(f"Valid Epochs : {len(epochs)}")
print(f"Epoch Shape  : {data.shape}")

# --------------------------------------------------
# Time Domain Features
# --------------------------------------------------

mean = data.mean(axis=(1,2))
std = data.std(axis=(1,2))
maximum = data.max(axis=(1,2))
minimum = data.min(axis=(1,2))
ptp = np.ptp(data, axis=(1,2))
rms = np.sqrt(np.mean(data**2, axis=(1,2)))

features = pd.DataFrame({
    "Mean": mean,
    "Std": std,
    "Max": maximum,
    "Min": minimum,
    "PeakToPeak": ptp,
    "RMS": rms
})

# --------------------------------------------------
# Save CSV
# --------------------------------------------------

csv_file = "features/time_domain_features.csv"
features.to_csv(csv_file, index=False)

print("CSV Saved.")

# --------------------------------------------------
# Save Report
# --------------------------------------------------

with open(
    "results/lab09_01_time_domain_features_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab09.1 - Time Domain Features\n")
    report.write("="*50 + "\n\n")

    report.write(f"Epochs : {len(epochs)}\n")
    report.write(f"Shape  : {data.shape}\n\n")

    report.write("Extracted Features\n")
    report.write("------------------\n")
    report.write("Mean\n")
    report.write("Standard Deviation\n")
    report.write("Maximum\n")
    report.write("Minimum\n")
    report.write("Peak-to-Peak\n")
    report.write("Root Mean Square\n")

print("Report Saved.")

# --------------------------------------------------
# Figure
# --------------------------------------------------

plt.figure(figsize=(8,4))
plt.plot(mean, marker='o')
plt.title("Mean Value of Each Epoch")
plt.xlabel("Epoch")
plt.ylabel("Mean")

plt.grid(True)

plt.savefig(
    "figures/lab09_time_features.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Figure Saved.")

shutil.copy(
    "figures/lab09_time_features.png",
    "docs/images/lab09_time_features.png"
)

print("Documentation Figure Saved.")

print("\nLab09.1 Finished Successfully.")
