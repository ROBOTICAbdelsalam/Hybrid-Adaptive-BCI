import os
import shutil
import matplotlib.pyplot as plt
import mne
from mne.datasets import eegbci

print("=" * 60)
print("Lab 08.3 - Baseline Correction")
print("=" * 60)

os.makedirs("results", exist_ok=True)
os.makedirs("figures", exist_ok=True)
os.makedirs("docs/images", exist_ok=True)

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

print("\nBaseline correction applied successfully.")
print(f"Valid Epochs : {len(epochs)}")
print(f"Epoch Shape  : {epochs.get_data().shape}")

with open(
    "results/lab08_03_baseline_correction_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab 08.3 - Baseline Correction\n")
    report.write("=" * 50 + "\n\n")
    report.write(f"Subject : {subject}\n")
    report.write(f"Run : {runs}\n\n")
    report.write("Baseline Window : (-0.2, 0.0) sec\n\n")
    report.write(f"Valid Epochs : {len(epochs)}\n")
    report.write(f"Epoch Shape : {epochs.get_data().shape}\n")

print("Report Saved.")

fig = epochs.average().plot(show=False)

fig.savefig(
    "figures/lab08_baseline_correction.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close(fig)

print("Figure Saved.")

shutil.copy(
    "figures/lab08_baseline_correction.png",
    "docs/images/lab08_baseline_correction.png"
)

print("Documentation Figure Saved.")
print("\nLab08.3 Finished Successfully.")
