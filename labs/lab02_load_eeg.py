from mne.datasets import eegbci
import mne

print("=" * 50)
print("Lab 02 - Download EEG Dataset")
print("=" * 50)

subject = 1
runs = [4]

files = eegbci.load_data(subject, runs)

print("\nDataset files:")
for f in files:
    print(f)
    