# Lab 14.1 – Live EEG Streaming

## Objective

The objective of this laboratory is to establish the first stage of the real-time Brain–Computer Interface (BCI) framework by simulating live EEG signal acquisition.

The laboratory generates a continuous multi-channel EEG stream, stores the acquired data, and prepares it for subsequent real-time signal processing.

---

## Background

Real-time Brain–Computer Interface systems continuously receive EEG signals from acquisition hardware such as OpenBCI, Muse, or Emotiv devices.

Since dedicated EEG hardware is not available during the current stage of development, this laboratory employs simulated EEG signals that reproduce the characteristics of continuous real-time acquisition.

The generated data provides a realistic environment for developing and validating the complete real-time processing pipeline before integrating physical EEG hardware.

---

## Python Script

```
labs/lab14_01_live_eeg_streaming.py
```

---

## Simulation Parameters

| Parameter | Value |
|-----------|-------|
| EEG Channels | 8 |
| Sampling Rate | 250 Hz |
| Streaming Duration | 5 Seconds |
| Total Samples | 1250 |

---

## Processing Steps

1. Initialize the real-time data directory.
2. Configure the streaming parameters.
3. Generate simulated EEG samples continuously.
4. Store each sample in memory.
5. Save the complete EEG stream.
6. Compute descriptive signal statistics.
7. Generate the streaming report.

---

## Output Files

### EEG Stream Dataset

```
realtime/data/live_eeg_stream.csv
```

### Streaming Report

```
realtime/results/lab14_01_stream_report.txt
```

---

## Experimental Result

The simulated EEG acquisition successfully generated:

| Metric | Value |
|---------|------:|
| Channels | **8** |
| Sampling Rate | **250 Hz** |
| Duration | **5 Seconds** |
| Total Samples | **1250** |

---

## Example Console Output

```
============================================================
Lab14.1 - Live EEG Streaming
============================================================

Channels      : 8
Sampling Rate : 250 Hz
Duration      : 5 Seconds

Streaming EEG...

Second 1
Second 2
Second 3
Second 4
Second 5

Live EEG Saved Successfully.

Dataset Shape

(1250, 8)

Report Saved.

Lab14.1 Finished Successfully.
```

---

## Generated Dataset

The generated dataset contains eight simulated EEG channels.

Example structure:

| EEG_1 | EEG_2 | EEG_3 | EEG_4 | EEG_5 | EEG_6 | EEG_7 | EEG_8 |
|------:|------:|------:|------:|------:|------:|------:|------:|
| ... | ... | ... | ... | ... | ... | ... | ... |

---

## Discussion

This laboratory represents the first stage of the real-time BCI pipeline by establishing a continuous EEG acquisition process.

Although simulated EEG signals were used, the overall software architecture is identical to that required for real EEG hardware.

When an actual EEG acquisition device becomes available, the simulated signal generation module can be replaced with hardware-specific streaming libraries such as BrainFlow or Lab Streaming Layer (LSL), while preserving the remaining processing pipeline.

---

## Conclusion

The real-time EEG streaming framework was successfully implemented.

A continuous eight-channel EEG stream was generated, stored, and analyzed using descriptive statistical measures.

The resulting dataset forms the input for the next laboratory, where real-time preprocessing techniques will be applied before feature extraction and classification.