from mne.datasets import eegbci
import mne
import matplotlib.pyplot as plt

print("=" * 50)
print("Lab 04 - Save EEG Figure")
print("=" * 50)

subject = 1
runs = [4]

files = eegbci.load_data(subject, runs)

raw = mne.io.read_raw_edf(files[0], preload=True)

fig = raw.plot(
    duration=5,
    n_channels=10,
    scalings="auto",
    show=False
)

plt.savefig("figures/lab04_raw_eeg.png", dpi=300)

print("Figure saved successfully!")

