import os
import pandas as pd
import mne

print("=" * 60)
print("Lab11.2 - Create Labels")
print("=" * 60)

os.makedirs("results", exist_ok=True)

# --------------------------------------------------
# Load CSP Dataset
# --------------------------------------------------

features = pd.read_csv("csp/csp_dataset.csv")

# --------------------------------------------------
# Load Epochs
# --------------------------------------------------

epochs = mne.read_epochs(
    "processed_data/subject01_run04-epo.fif",
    preload=True,
    verbose=False
)

# --------------------------------------------------
# Extract Labels
# --------------------------------------------------

labels = epochs.events[:, 2]

print("Number of Labels :", len(labels))
print("Unique Labels    :", sorted(set(labels)))

# --------------------------------------------------
# Check Sizes
# --------------------------------------------------

if len(labels) != len(features):
    raise ValueError(
        f"Mismatch detected!\n"
        f"Features: {len(features)}\n"
        f"Labels  : {len(labels)}"
    )

# --------------------------------------------------
# Add Labels
# --------------------------------------------------

features["Label"] = labels

# --------------------------------------------------
# Save Dataset
# --------------------------------------------------

features.to_csv(
    "csp/csp_dataset_with_labels.csv",
    index=False
)

# --------------------------------------------------
# Report
# --------------------------------------------------

with open(
    "results/lab11_02_create_labels_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab11.2 - Create Labels\n")
    report.write("=" * 55 + "\n\n")

    report.write(f"Samples : {len(features)}\n")
    report.write(f"Classes : {sorted(set(labels))}\n")
    report.write(f"Features: {features.shape[1]-1}\n")

print("Dataset with Labels Saved.")
print("Report Saved.")

print("\nLab11.2 Finished Successfully.")
