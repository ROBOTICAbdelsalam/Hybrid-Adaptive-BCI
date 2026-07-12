import os
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mne
from scipy.stats import skew, kurtosis

print("="*60)
print("Lab09.5 - Statistical Feature Extraction")
print("="*60)

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

print(f"Epochs : {len(epochs)}")
print(f"Shape  : {data.shape}")

# --------------------------------------------------
# Flatten each epoch
# --------------------------------------------------

X = data.reshape(len(data), -1)

# --------------------------------------------------
# Statistical Features
# --------------------------------------------------

mean = X.mean(axis=1)
std = X.std(axis=1)
var = X.var(axis=1)
median = np.median(X, axis=1)
sk = skew(X, axis=1)
kt = kurtosis(X, axis=1)

df = pd.DataFrame({
    "Mean": mean,
    "Std": std,
    "Variance": var,
    "Median": median,
    "Skewness": sk,
    "Kurtosis": kt
})

# --------------------------------------------------
# Save CSV
# --------------------------------------------------

df.to_csv(
    "features/statistical_features.csv",
    index=False
)

print("CSV Saved.")

# --------------------------------------------------
# Save Report
# --------------------------------------------------

with open(
    "results/lab09_05_statistical_features_report.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write("Lab09.5 Statistical Features\n")
    f.write("="*50+"\n\n")

    f.write(f"Epochs : {len(epochs)}\n")
    f.write(f"Shape : {data.shape}\n\n")

    f.write("Extracted Features\n")
    f.write("------------------\n")
    f.write("Mean\n")
    f.write("Standard Deviation\n")
    f.write("Variance\n")
    f.write("Median\n")
    f.write("Skewness\n")
    f.write("Kurtosis\n")

print("Report Saved.")

# --------------------------------------------------
# Figure
# --------------------------------------------------

plt.figure(figsize=(8,4))
plt.plot(mean, marker="o", label="Mean")
plt.plot(std, marker="s", label="Std")

plt.title("Statistical Features")
plt.xlabel("Epoch")
plt.ylabel("Value")
plt.grid(True)
plt.legend()

plt.savefig(
    "figures/lab09_statistical_features.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Figure Saved.")

shutil.copy(
    "figures/lab09_statistical_features.png",
    "docs/images/lab09_statistical_features.png"
)

print("Documentation Figure Saved.")

print("\nLab09.5 Finished Successfully.")
