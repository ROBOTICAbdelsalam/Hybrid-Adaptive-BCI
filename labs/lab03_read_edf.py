from mne.datasets import eegbci
import mne

print("=" * 50)
print("Lab 03 - Read EEG EDF File")
print("=" * 50)

subject = 1
runs = [4]

files = eegbci.load_data(subject, runs)

print("\nLoading file:")
print(files[0])

raw = mne.io.read_raw_edf(files[0], preload=True)

print("\nDataset loaded successfully!")

print(raw)