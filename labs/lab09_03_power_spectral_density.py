import os
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mne

print("=" * 60)
print("Lab 09.3 - Power Spectral Density")
print("=" * 60)

# --------------------------------------------------
# Create folders
# --------------------------------------------------
os.makedirs("results", exist_ok=True)
os.makedirs("figures", exist_ok=True)
os.makedirs("features", exist_ok=True)
os.makedirs("docs/images", exist_ok=True)

# --------------------------------------------------
# Load Processed Epochs
# --------------------------------------------------
epochs = mne.read_epochs(
    "processed_data/subject01_run04-epo.fif",
    preload=True
)

data = epochs.get_data()

print(f"Valid Epochs : {len(epochs)}")
print(f"Epoch Shape  : {data.shape}")

# --------------------------------------------------
# Compute PSD
# --------------------------------------------------
spectrum = epochs.compute_psd(
    method="welch",
    fmin=1,
    fmax=40
)

psds = spectrum.get_data()
freqs = spectrum.freqs

mean_psd = psds.mean(axis=(1,2))
max_psd = psds.max(axis=(1,2))

features = pd.DataFrame({
    "MeanPSD": mean_psd,
    "MaxPSD": max_psd
})

features.to_csv(
    "features/psd_features.csv",
    index=False
)

print("PSD CSV Saved.")

# --------------------------------------------------
# Report
# --------------------------------------------------
with open(
    "results/lab09_03_psd_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab09.3 - Power Spectral Density\n")
    report.write("=" * 50 + "\n\n")

    report.write(f"Epochs : {len(epochs)}\n")
    report.write(f"Shape  : {data.shape}\n")
    report.write(f"Frequency Range : {freqs[0]:.1f} - {freqs[-1]:.1f} Hz\n")

print("Report Saved.")

# --------------------------------------------------
# Figure
# --------------------------------------------------
plt.figure(figsize=(8,4))
plt.plot(mean_psd, marker="o")
plt.title("Mean PSD per Epoch")
plt.xlabel("Epoch")
plt.ylabel("Mean PSD")
plt.grid(True)

plt.savefig(
    "figures/lab09_psd.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Figure Saved.")

shutil.copy(
    "figures/lab09_psd.png",
    "docs/images/lab09_psd.png"
)

print("Documentation Figure Saved.")

print("\nLab09.3 Finished Successfully.")
