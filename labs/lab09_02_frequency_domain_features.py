import os
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mne
from mne.datasets import eegbci

print("=" * 60)
print("Lab 09.2 - Frequency Domain Feature Extraction")
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
# FFT Feature Extraction
# --------------------------------------------------

fft_data = np.abs(np.fft.rfft(data, axis=-1))

mean_spectrum = fft_data.mean(axis=(1,2))
max_spectrum = fft_data.max(axis=(1,2))
dominant_frequency_index = fft_data.mean(axis=1).argmax(axis=1)

features = pd.DataFrame({
    "MeanSpectrum": mean_spectrum,
    "MaxSpectrum": max_spectrum,
    "DominantFrequencyIndex": dominant_frequency_index
})

csv_file = "features/frequency_domain_features.csv"
features.to_csv(csv_file, index=False)

print("CSV Saved.")

# --------------------------------------------------
# Save Report
# --------------------------------------------------

with open(
    "results/lab09_02_frequency_domain_features_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab09.2 - Frequency Domain Features\n")
    report.write("="*50 + "\n\n")

    report.write(f"Epochs : {len(epochs)}\n")
    report.write(f"Shape  : {data.shape}\n\n")

    report.write("Extracted Features\n")
    report.write("------------------\n")
    report.write("Mean Spectrum\n")
    report.write("Maximum Spectrum\n")
    report.write("Dominant Frequency Index\n")

print("Report Saved.")

# --------------------------------------------------
# Figure
# --------------------------------------------------

plt.figure(figsize=(8,4))
plt.plot(mean_spectrum, marker='o')
plt.title("Mean Spectrum of Each Epoch")
plt.xlabel("Epoch")
plt.ylabel("Mean Spectrum")
plt.grid(True)

plt.savefig(
    "figures/lab09_frequency_features.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Figure Saved.")

shutil.copy(
    "figures/lab09_frequency_features.png",
    "docs/images/lab09_frequency_features.png"
)

print("Documentation Figure Saved.")

print("\nLab09.2 Finished Successfully.")
