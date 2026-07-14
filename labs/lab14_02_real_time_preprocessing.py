import os
import pandas as pd
import numpy as np
from scipy.signal import butter, filtfilt

print("=" * 60)
print("Lab14.2 - Real-Time Preprocessing")
print("=" * 60)

# --------------------------------------------------
# Create Folder
# --------------------------------------------------

os.makedirs("realtime/results", exist_ok=True)

# --------------------------------------------------
# Load EEG Stream
# --------------------------------------------------

input_file = "realtime/data/live_eeg_stream.csv"

if not os.path.exists(input_file):

    print("Live EEG stream not found.")
    exit()

eeg = pd.read_csv(input_file)

print("\nOriginal Dataset Shape")

print(eeg.shape)

# --------------------------------------------------
# Remove DC Offset
# --------------------------------------------------

eeg = eeg - eeg.mean()

print("\nDC Offset Removed.")

# --------------------------------------------------
# Band-pass Filter
# --------------------------------------------------

sampling_rate = 250

lowcut = 8

highcut = 30

nyquist = sampling_rate / 2

b, a = butter(
    4,
    [lowcut / nyquist,
     highcut / nyquist],
    btype="band"
)

filtered = filtfilt(
    b,
    a,
    eeg.values,
    axis=0
)

filtered = pd.DataFrame(
    filtered,
    columns=eeg.columns
)

print("Band-pass Filter Applied.")

# --------------------------------------------------
# Save Processed Signal
# --------------------------------------------------

output_file = "realtime/data/preprocessed_eeg.csv"

filtered.to_csv(
    output_file,
    index=False
)

print("\nPreprocessed EEG Saved Successfully.")

# --------------------------------------------------
# Statistics
# --------------------------------------------------

print("\nProcessed Dataset Shape")

print(filtered.shape)

print("\nSignal Statistics")

print(filtered.describe())

# --------------------------------------------------
# Save Report
# --------------------------------------------------

with open(

    "realtime/results/lab14_02_preprocessing_report.txt",

    "w",

    encoding="utf-8"

) as report:

    report.write("Lab14.2 - Real-Time Preprocessing\n")

    report.write("=" * 60 + "\n\n")

    report.write(f"Input File : {input_file}\n")

    report.write(f"Output File : {output_file}\n")

    report.write(f"Sampling Rate : {sampling_rate}\n")

    report.write(f"Band-pass : {lowcut}-{highcut} Hz\n")

    report.write(f"Channels : {filtered.shape[1]}\n")

    report.write(f"Samples : {filtered.shape[0]}\n")

print("\nReport Saved.")

print("\nLab14.2 Finished Successfully.")