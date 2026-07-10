import os
import mne
from mne.datasets import eegbci
from mne.preprocessing import ICA

print("=" * 60)
print("Lab 07.3 - Manual ICA Component Selection")
print("=" * 60)

# -------------------------------------------------
# Load EEG Dataset
# -------------------------------------------------

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

# -------------------------------------------------
# EEG Filtering
# -------------------------------------------------

raw.filter(
    l_freq=1.0,
    h_freq=40.0
)

# -------------------------------------------------
# Train ICA
# -------------------------------------------------

print("\nTraining ICA model...\n")

ica = ICA(
    n_components=20,
    random_state=42,
    method="fastica"
)

ica.fit(raw)

# -------------------------------------------------
# Manual Component Selection
# -------------------------------------------------

print("=" * 60)
print("Detected ICA Components")
print("=" * 60)

for component in range(20):
    print(f"ICA{component:03d}")

print("\nOpen the following figure:")
print("figures/lab07_ica_components_page_1.png")

print("\nInspect every ICA component carefully.")

print("\nTypical artifacts:")
print("- Eye Blink")
print("- Eye Movement")
print("- Muscle Activity")
print("- ECG")
print("- Power Line Noise")

print("\nAfter visual inspection, write the component")
print("numbers that should be removed.")

print("\nExample:")
print("[0, 7]")

selected_components = []

print("\nSelected Components:")
print(selected_components)

# -------------------------------------------------
# Save Report
# -------------------------------------------------

os.makedirs("results", exist_ok=True)

report = f"""
Lab 07.3 - Manual ICA Component Selection
=========================================

Dataset
-------
EEGBCI
Subject : 1
Run     : 4

Method
------
Manual ICA Component Inspection

Algorithm
---------
FastICA

Number of Components
--------------------
20

Purpose
-------
Identify artifact-related ICA components manually before signal reconstruction.

Output Figure
-------------
figures/lab07_ica_components_page_1.png

Selected Components
-------------------
{selected_components}

Status
------
Waiting for manual artifact selection.
"""

report_path = "results/lab07_03_manual_component_selection_report.txt"

with open(report_path, "w") as file:
    file.write(report)

print("\nReport saved successfully.")
print(report_path)

print("\nLab 07.3 completed successfully.")