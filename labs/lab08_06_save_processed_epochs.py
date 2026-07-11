import os
import shutil
import mne
from mne.datasets import eegbci

print("=" * 60)
print("Lab 08.6 - Save Processed Epochs")
print("=" * 60)

# --------------------------------------------------
# Create folders
# --------------------------------------------------
os.makedirs("results", exist_ok=True)
os.makedirs("processed_data", exist_ok=True)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------
subject = 1
runs = [4]

files = eegbci.load_data(subject, runs)

raw = mne.io.read_raw_edf(files[0], preload=True)

events, event_id = mne.events_from_annotations(raw)

# --------------------------------------------------
# Create Epochs
# --------------------------------------------------
epochs = mne.Epochs(
    raw,
    events,
    event_id=event_id,
    tmin=-0.2,
    tmax=0.8,
    baseline=(-0.2, 0),
    preload=True
)

# --------------------------------------------------
# Save Epochs
# --------------------------------------------------
output_file = "processed_data/subject01_run04-epo.fif"
epochs.save(output_file, overwrite=True)

print(f"Epochs saved to: {output_file}")

# --------------------------------------------------
# Save Report
# --------------------------------------------------
with open(
    "results/lab08_06_save_processed_epochs_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab 08.6 - Save Processed Epochs\n")
    report.write("=" * 50 + "\n\n")
    report.write(f"Output File : {output_file}\n")
    report.write(f"Valid Epochs : {len(epochs)}\n")
    report.write(f"Epoch Shape : {epochs.get_data().shape}\n")

print("Report Saved.")
print("\nLab08.6 Finished Successfully.")
