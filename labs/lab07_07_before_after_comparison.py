import os
import matplotlib.pyplot as plt
import mne
from mne.datasets import eegbci
from mne.preprocessing import ICA

print("=" * 60)
print("Lab 07.7 - Before vs After Comparison")
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

montage = mne.channels.make_standard_montage(
    "standard_1005"
)

raw.set_montage(montage)

# --------------------------------------------------
# Band-pass Filter
# --------------------------------------------------

print("Filtering EEG...")

raw.filter(
    l_freq=1.0,
    h_freq=40.0
)

print("Filtering completed.")

# --------------------------------------------------
# ICA Training
# --------------------------------------------------

print("Training ICA model...")

ica_manual = ICA(
    n_components=20,
    random_state=42,
    method="fastica"
)

ica_manual.fit(raw)

print("Manual ICA model completed.")

ica_auto = ICA(
    n_components=20,
    random_state=42,
    method="fastica"
)

ica_auto.fit(raw)

print("Automatic ICA model completed.")

# --------------------------------------------------
# Manual Artifact Removal
# --------------------------------------------------

print()

print("Enter ICA components to remove manually.")
print("Example: 0,1")

user_input = input("Components: ").strip()

if user_input == "":
    manual_components = []
else:
    manual_components = [
        int(x.strip())
        for x in user_input.split(",")
    ]

manual_raw = raw.copy()

ica_manual.exclude = manual_components

ica_manual.apply(manual_raw)

print()

print("Manual components removed.")

# --------------------------------------------------
# Automatic Artifact Removal
# --------------------------------------------------

auto_raw = raw.copy()

auto_components = []

eog_channels = mne.pick_types(
    raw.info,
    eog=True
)

if len(eog_channels) > 0:

    auto_components, scores = ica_auto.find_bads_eog(raw)

    ica_auto.exclude = auto_components

    ica_auto.apply(auto_raw)

    print("Automatic artifact removal completed.")

else:

    print("No EOG channel found.")
    print("Automatic artifact removal skipped.")

print()
print("Data preparation completed.")
# --------------------------------------------------
# Create Comparison Figure
# --------------------------------------------------

print("Generating comparison figures...")

# Original EEG
fig = raw.plot(
    show=False,
    duration=10,
    scalings="auto"
)

fig.savefig(
    "figures/lab07_original_eeg.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close(fig)

# Manual Clean EEG
fig = manual_raw.plot(
    show=False,
    duration=10,
    scalings="auto"
)

fig.savefig(
    "figures/lab07_manual_cleaned_eeg.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close(fig)

# Automatic Clean EEG
fig = auto_raw.plot(
    show=False,
    duration=10,
    scalings="auto"
)

fig.savefig(
    "figures/lab07_auto_cleaned_eeg.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close(fig)

print("All figures saved successfully.")

# --------------------------------------------------
# Create Report
# --------------------------------------------------

report = f"""
Lab 07.7 - Before vs After Comparison
============================================================

Dataset
-------
EEGBCI

Subject
-------
1

Run
---
4

Manual Components Removed
-------------------------
{manual_components}

Automatic Components Removed
----------------------------
{auto_components}

Generated Figures
-----------------

figures/lab07_original_eeg.png

figures/lab07_manual_cleaned_eeg.png

figures/lab07_auto_cleaned_eeg.png

Summary
-------

Original EEG:
Raw EEG after filtering.

Manual ICA:
Artifacts removed using manually selected ICA components.

Automatic ICA:
Artifacts removed automatically when EOG channels are available.
For the EEGBCI dataset, no dedicated EOG channel exists,
therefore automatic removal was skipped.

Status
------

Lab 07.7 completed successfully.
"""

report_path = "results/lab07_07_before_after_comparison_report.txt"

with open(report_path, "w") as file:
    file.write(report)

print("Report saved successfully.")
print(report_path)

print("=" * 60)
print("Lab 07.7 completed successfully.")
print("=" * 60)
if len(eog_channels) > 0:

    auto_components, scores = ica_auto.find_bads_eog(raw)

    ica_auto.exclude = auto_components

    ica_auto.apply(auto_raw)

    fig = auto_raw.plot(
        show=False,
        duration=10,
        scalings="auto"
    )

    fig.savefig(
        "figures/lab07_auto_cleaned_eeg.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

    print("Automatic artifact removal completed.")

else:

    print("No EOG channel found.")
    print("Automatic artifact removal skipped.")