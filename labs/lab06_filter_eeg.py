from mne.datasets import eegbci
import mne
import matplotlib.pyplot as plt

print("=" * 50)
print("Lab 06 - EEG Filtering")
print("=" * 50)

# Subject
subject = 1
runs = [4]

# Download dataset
files = eegbci.load_data(subject, runs)

# Read EDF file
raw = mne.io.read_raw_edf(files[0], preload=True)

print("\nApplying Band-pass Filter...")

# Apply filter
raw.filter(l_freq=1.0, h_freq=40.0)

print("Filtering completed.")

# Plot first 5 seconds
fig = raw.plot(
    duration=5,
    n_channels=20,
    show=False
)

# Save figure
fig.savefig("figures/lab06_filtered_eeg.png", dpi=300)

print("Figure saved to figures/lab06_filtered_eeg.png")