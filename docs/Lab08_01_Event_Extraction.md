import mne
from mne.datasets import eegbci

print("==========================================")
print("Lab 08.1 - Event Extraction")
print("==========================================")

subject = 1
runs = [4]

files = eegbci.load_data(subject, runs)

raw = mne.io.read_raw_edf(files[0], preload=True)

events, event_id = mne.events_from_annotations(raw)

print("\nEvent IDs:")
print(event_id)

print("\nNumber of events:")
print(len(events))

print("\nFirst 10 events:")
print(events[:10])