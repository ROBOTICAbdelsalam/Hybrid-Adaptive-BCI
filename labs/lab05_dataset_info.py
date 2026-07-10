from mne.datasets import eegbci
import mne

print("=" * 50)
print("Lab 05 - EEG Dataset Information")
print("=" * 50)

subject = 1
runs = [4]

files = eegbci.load_data(subject, runs)

raw = mne.io.read_raw_edf(files[0], preload=True)

print("\nDataset Information")
print("-" * 50)

print(f"Number of channels : {len(raw.ch_names)}")
print(f"Sampling frequency : {raw.info['sfreq']} Hz")
print(f"Recording duration : {raw.times[-1]:.2f} seconds")

print("\nChannel Names")
print(raw.ch_names)

print("\nChannel Types")
print(raw.get_channel_types())