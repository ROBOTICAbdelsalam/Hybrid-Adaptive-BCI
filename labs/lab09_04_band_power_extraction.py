import os
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mne

print("="*60)
print("Lab09.4 - Band Power Extraction")
print("="*60)

os.makedirs("results", exist_ok=True)
os.makedirs("figures", exist_ok=True)
os.makedirs("features", exist_ok=True)
os.makedirs("docs/images", exist_ok=True)

epochs = mne.read_epochs(
    "processed_data/subject01_run04-epo.fif",
    preload=True
)

print(f"Epochs : {len(epochs)}")

bands = {
    "Delta": (1,4),
    "Theta": (4,8),
    "Alpha": (8,13),
    "Beta": (13,30),
    "Gamma": (30,40)
}

results = {}

for band,(fmin,fmax) in bands.items():

    spectrum = epochs.compute_psd(
        method="welch",
        fmin=fmin,
        fmax=fmax
    )

    psd = spectrum.get_data()

    results[band] = psd.mean(axis=(1,2))

df = pd.DataFrame(results)

df.to_csv(
    "features/band_power_features.csv",
    index=False
)

print("Band Power CSV Saved.")

with open(
    "results/lab09_04_band_power_report.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write("Lab09.4 Band Power Extraction\n")
    f.write("="*50+"\n\n")

    f.write(f"Epochs : {len(epochs)}\n\n")

    for band,(a,b) in bands.items():
        f.write(f"{band}: {a}-{b} Hz\n")

print("Report Saved.")

plt.figure(figsize=(10,5))

for band in df.columns:
    plt.plot(df[band],label=band)

plt.title("Band Power Across Epochs")
plt.xlabel("Epoch")
plt.ylabel("Mean Power")
plt.legend()

plt.grid(True)

plt.savefig(
    "figures/lab09_band_power.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

shutil.copy(
    "figures/lab09_band_power.png",
    "docs/images/lab09_band_power.png"
)

print("Figure Saved.")
print("Documentation Figure Saved.")

print("\nLab09.4 Finished Successfully.")
