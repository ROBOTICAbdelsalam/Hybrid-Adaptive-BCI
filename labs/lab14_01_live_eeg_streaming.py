import os
import time
import numpy as np
import pandas as pd

print("=" * 60)
print("Lab14.1 - Live EEG Streaming")
print("=" * 60)

# --------------------------------------------------
# Create Folder
# --------------------------------------------------

os.makedirs("realtime/data", exist_ok=True)

# --------------------------------------------------
# Simulation Parameters
# --------------------------------------------------

channels = 8
sampling_rate = 250
duration = 5

samples = sampling_rate * duration

print(f"\nChannels      : {channels}")
print(f"Sampling Rate : {sampling_rate} Hz")
print(f"Duration      : {duration} Seconds")

print("\nStreaming EEG...\n")

# --------------------------------------------------
# Simulated EEG Stream
# --------------------------------------------------

stream = []

for i in range(samples):

    eeg = np.random.randn(channels)

    stream.append(eeg)

    if i % sampling_rate == 0:

        print(f"Second {i//sampling_rate + 1}")

    time.sleep(0.001)

stream = np.array(stream)

# --------------------------------------------------
# Save Data
# --------------------------------------------------

columns = []

for i in range(channels):

    columns.append(f"EEG_{i+1}")

df = pd.DataFrame(stream, columns=columns)

output = "realtime/data/live_eeg_stream.csv"

df.to_csv(output, index=False)

print("\nLive EEG Saved Successfully.")

print("\nDataset Shape")

print(df.shape)

# --------------------------------------------------
# Statistics
# --------------------------------------------------

print("\nSignal Statistics")

print(df.describe())

# --------------------------------------------------
# Save Report
# --------------------------------------------------

with open(

    "realtime/results/lab14_01_stream_report.txt",

    "w",

    encoding="utf-8"

) as report:

    report.write("Lab14.1 - Live EEG Streaming\n")

    report.write("=" * 60 + "\n\n")

    report.write(f"Channels : {channels}\n")

    report.write(f"Sampling Rate : {sampling_rate}\n")

    report.write(f"Duration : {duration}\n")

    report.write(f"Samples : {samples}\n")

    report.write(f"Output File : {output}\n")

print("\nReport Saved.")

print("\nLab14.1 Finished Successfully.")