import os
import shutil
import matplotlib.pyplot as plt
import mne
from mne.datasets import eegbci

print("=" * 60)
print("Lab 08.4 - Epoch Visualization")
print("=" * 60)

# --------------------------------------------------
# Create folders
# --------------------------------------------------
os.makedirs("results", exist_ok=True)
os.makedirs("figures", exist_ok=True)
os.makedirs("docs/images", exist_ok=True)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------
subject = 1
runs = [4]

files = eegbci.load_data(subject, runs)

raw = mne.io.read_raw_edf(files[0], preload=True)

events, event_id = mne.events_from_annotations(raw)

epochs = mne.Epochs(
    raw,
    events,
    event_id=event_id,
    tmin=-0.2,
    tmax=0.8,
    baseline=(-0.2, 0),
    preload=True
)

print(f"\nEpochs Ready: {len(epochs)}")

# --------------------------------------------------
# Average Epoch
# --------------------------------------------------
evoked = epochs.average()

fig = evoked.plot(show=False)

fig.savefig(
    "figures/lab08_epoch_visualization.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close(fig)

print("Visualization Figure Saved.")

# --------------------------------------------------
# Copy Figure
# --------------------------------------------------
shutil.copy(
    "figures/lab08_epoch_visualization.png",
    "docs/images/lab08_epoch_visualization.png"
)

print("Documentation Figure Saved.")

# --------------------------------------------------
# Save Report
# --------------------------------------------------
with open(
    "results/lab08_04_epoch_visualization_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab 08.4 - Epoch Visualization\n")
    report.write("=" * 50 + "\n\n")

    report.write(f"Subject : {subject}\n")
    report.write(f"Run     : {runs}\n\n")

    report.write(f"Valid Epochs : {len(epochs)}\n")
    report.write(f"Epoch Shape  : {epochs.get_data().shape}\n\n")

    report.write("Visualization completed successfully.\n")

print("Report Saved.")

print("\nLab08.4 Finished Successfully.")
