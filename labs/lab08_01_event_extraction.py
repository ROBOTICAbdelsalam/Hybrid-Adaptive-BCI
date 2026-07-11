import os
import matplotlib.pyplot as plt
import mne
from mne.datasets import eegbci

print("=" * 60)
print("Lab 08.1 - Event Extraction")
print("=" * 60)

# ------------------------------------------------
# Create folders
# ------------------------------------------------
os.makedirs("results", exist_ok=True)
os.makedirs("figures", exist_ok=True)

# ------------------------------------------------
# Load dataset
# ------------------------------------------------
subject = 1
runs = [4]

files = eegbci.load_data(subject, runs)

raw = mne.io.read_raw_edf(files[0], preload=True)

# ------------------------------------------------
# Extract Events
# ------------------------------------------------
events, event_id = mne.events_from_annotations(raw)

print("\nEvent IDs:")
print(event_id)

print("\nNumber of events:")
print(len(events))

print("\nFirst 10 events:")
print(events[:10])

# ------------------------------------------------
# Save Report
# ------------------------------------------------
with open("results/lab08_01_event_extraction_report.txt", "w") as f:

    f.write("Lab 08.1 - Event Extraction\n")
    f.write("="*50 + "\n\n")

    f.write("Event IDs\n")
    f.write(str(event_id))
    f.write("\n\n")

    f.write("Number of events\n")
    f.write(str(len(events)))
    f.write("\n\n")

    f.write("First 10 Events\n")
    f.write(str(events[:10]))

print("\nReport Saved.")

# ------------------------------------------------
# Plot Events
# ------------------------------------------------

fig = mne.viz.plot_events(
    events,
    sfreq=raw.info["sfreq"],
    first_samp=raw.first_samp,
    show=False
)

fig.savefig(
    "figures/lab08_events.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close(fig)

print("Figure Saved.")

print("\nLab08.1 Finished Successfully.")