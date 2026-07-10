import os
import matplotlib.pyplot as plt
import mne
from mne.datasets import eegbci
from mne.preprocessing import ICA

print("=" * 60)
print("Lab 07.5 - ICA Artifact Removal")
print("=" * 60)

# --------------------------------------------------
# Create Output Directories
# --------------------------------------------------

os.makedirs("figures", exist_ok=True)
os.makedirs("results", exist_ok=True)

# --------------------------------------------------
# Load EEG Dataset
# --------------------------------------------------

subject = 1
runs = [4]

files = eegbci.load_data(subject, runs)

raw = mne.io.read_raw_edf(
    files[0],
    preload=True
)

eegbci.standardize(raw)

montage = mne.channels.make_standard_montage("standard_1005")
raw.set_montage(montage)

# --------------------------------------------------
# Band-pass Filter
# --------------------------------------------------

print("Applying band-pass filter...")

raw.filter(
    l_freq=1.0,
    h_freq=40.0
)

print("Filtering completed.")

# --------------------------------------------------
# Train ICA
# --------------------------------------------------

print("Training ICA model...")

ica = ICA(
    n_components=20,
    random_state=42,
    method="fastica"
)

ica.fit(raw)

print("ICA model trained successfully.")

# --------------------------------------------------
# User Selection
# --------------------------------------------------

print()
print("Enter ICA components to remove.")
print("Example: 0,1")
print("Press Enter to skip.")

user_input = input("Components: ").strip()

if user_input == "":
    selected_components = []
else:
    selected_components = [
        int(x.strip())
        for x in user_input.split(",")
    ]

print()
print("Selected Components:")
print(selected_components)

# --------------------------------------------------
# Remove Artifacts
# --------------------------------------------------

clean_raw = raw.copy()

ica.exclude = selected_components

ica.apply(clean_raw)

print("Artifacts removed successfully.")

# --------------------------------------------------
# Save Figure
# --------------------------------------------------

fig = clean_raw.plot(
    show=False,
    duration=10,
    scalings="auto"
)

fig.savefig(
    "figures/lab07_cleaned_eeg.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close(fig)

print("Figure saved successfully.")

# --------------------------------------------------
# Save Report
# --------------------------------------------------

report = f"""
Lab 07.5 - ICA Artifact Removal
============================================================

Dataset:
EEGBCI

Subject:
1

Run:
4

Method:
Independent Component Analysis (ICA)

Algorithm:
FastICA

Removed Components:
{selected_components}

Output Figure:
figures/lab07_cleaned_eeg.png

Status:
Artifact removal completed successfully.
"""

report_path = "results/lab07_05_artifact_removal_report.txt"

with open(report_path, "w") as file:
    file.write(report)

print("Report saved successfully.")
print(report_path)

print("=" * 60)
print("Lab 07.5 completed successfully.")
print("=" * 60)