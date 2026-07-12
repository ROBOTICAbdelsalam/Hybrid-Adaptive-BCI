import os
import shutil
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("Lab10.3 - Transform EEG Signals")
print("=" * 60)

os.makedirs("figures", exist_ok=True)
os.makedirs("results", exist_ok=True)
os.makedirs("docs/images", exist_ok=True)

# --------------------------------------------------
# Load CSP Features
# --------------------------------------------------

df = pd.read_csv("csp/csp_features.csv")

print(df.head())

# --------------------------------------------------
# Visualization
# --------------------------------------------------

plt.figure(figsize=(10,5))

for column in df.columns:
    plt.plot(df[column], label=column)

plt.title("CSP Features Across EEG Epochs")
plt.xlabel("Epoch")
plt.ylabel("Feature Value")
plt.legend()
plt.grid(True)

plt.savefig(
    "figures/lab10_csp_features.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

shutil.copy(
    "figures/lab10_csp_features.png",
    "docs/images/lab10_csp_features.png"
)

print("Figure Saved.")

# --------------------------------------------------
# Report
# --------------------------------------------------

with open(
    "results/lab10_03_transform_eeg_signals_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab10.3 - Transform EEG Signals\n")
    report.write("="*50+"\n\n")

    report.write(f"Samples : {df.shape[0]}\n")
    report.write(f"Features: {df.shape[1]}\n")

print("Report Saved.")

print("\nLab10.3 Finished Successfully.")
