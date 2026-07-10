import os
import mne
from mne.datasets import eegbci
from mne.preprocessing import ICA

print("=" * 60)
print("Lab 07.4 - Automatic ICA Component Detection")
print("=" * 60)

# --------------------------------------------------
# Create Output Directory
# --------------------------------------------------

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
# Automatic Detection
# --------------------------------------------------

print("\nSearching for EOG channels...")

report = []

report.append("Lab 07.4 - Automatic ICA Component Detection")
report.append("=" * 60)
report.append("")
report.append("Dataset : EEGBCI")
report.append("Subject : 1")
report.append("Run     : 4")
report.append("")
report.append("Detection Method : Automatic")
report.append("")

eog_channels = mne.pick_types(
    raw.info,
    eog=True
)

if len(eog_channels) == 0:

    print("No dedicated EOG channel was found.")
    print("Automatic detection cannot be performed.")

    report.append("Result")
    report.append("------")
    report.append("No dedicated EOG channel found.")
    report.append("Automatic component detection skipped.")
    report.append("")
    report.append("Recommendation")
    report.append("--------------")
    report.append("Use manual ICA selection.")
    report.append("Or use an EEG dataset with EOG channels.")

else:

    eog_indices, scores = ica.find_bads_eog(raw)

    print("\nSuggested Components:")
    print(eog_indices)

    report.append("Detected Components")
    report.append("-------------------")
    report.append(str(eog_indices))
    report.append("")
    report.append("Scores")
    report.append("------")
    report.append(str(scores))

# --------------------------------------------------
# Save Report
# --------------------------------------------------

report_path = "results/lab07_04_auto_component_detection_report.txt"

with open(report_path, "w") as file:
    file.write("\n".join(report))

print("\nReport saved successfully.")
print(report_path)

print("=" * 60)
print("Lab 07.4 completed successfully.")
print("=" * 60)