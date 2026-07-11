import os
import shutil
import matplotlib.pyplot as plt
import mne
from mne.datasets import eegbci

print("=" * 60)
print("Lab 08.2 - Epoch Creation")
print("=" * 60)

# ------------------------------------------------
# Load EEG Dataset
# ------------------------------------------------

subject = 1
runs = [4]

files = eegbci.load_data(subject, runs)

raw = mne.io.read_raw_edf(files[0], preload=True)

events, event_id = mne.events_from_annotations(raw)

# ------------------------------------------------
# Create Epochs
# ------------------------------------------------

epochs = mne.Epochs(
    raw,
    events,
    event_id=event_id,
    tmin=-0.2,
    tmax=0.8,
    baseline=(None, 0),
    preload=True
)

print("\nEpochs created successfully.")
print(f"Number of Epochs : {len(epochs)}")
print(f"Epoch Shape      : {epochs.get_data().shape}")

# ------------------------------------------------
# Create folders
# ------------------------------------------------

os.makedirs("results", exist_ok=True)
os.makedirs("figures", exist_ok=True)
os.makedirs("docs/images", exist_ok=True)

# ------------------------------------------------
# Save Report
# ------------------------------------------------

with open(
    "results/lab08_02_epoch_creation_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab 08.2 - Epoch Creation\n")
    report.write("=" * 50 + "\n\n")

    report.write(f"Subject : {subject}\n")
    report.write(f"Run     : {runs}\n\n")

    report.write(f"Number of Epochs : {len(epochs)}\n")
    report.write(f"Epoch Shape      : {epochs.get_data().shape}\n\n")

    report.write("Event IDs\n")
    report.write(str(event_id))

print("Report Saved.")

# ------------------------------------------------
# Save Figure
# ------------------------------------------------

fig = epochs.average().plot(show=False)

fig.savefig(
    "figures/lab08_epochs.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close(fig)

print("Figure Saved.")

# ------------------------------------------------
# Copy Figure
# ------------------------------------------------

shutil.copy(
    "figures/lab08_epochs.png",
    "docs/images/lab08_epochs.png"
)

print("Documentation Figure Saved.")

print("\nLab 08.2 Finished Successfully.")