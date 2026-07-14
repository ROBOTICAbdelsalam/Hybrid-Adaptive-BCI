# Lab 14.2 – Real-Time Preprocessing

## Objective

The objective of this laboratory is to preprocess the continuously acquired EEG signals before feature extraction and real-time classification.

The preprocessing stage removes unwanted signal components, eliminates DC offset, and applies a band-pass filter to preserve the EEG frequency bands associated with motor imagery.

---

## Background

Raw EEG signals contain various types of noise and unwanted frequency components originating from electrode drift, muscle activity, electrical interference, and environmental artifacts.

To improve classification performance, EEG signals must be preprocessed before feature extraction.

In this laboratory, two preprocessing operations are applied:

- DC Offset Removal
- Band-pass Filtering (8–30 Hz)

The selected frequency range preserves the Mu (8–13 Hz) and Beta (13–30 Hz) rhythms, which are widely used in Motor Imagery Brain–Computer Interface applications.

---

## Python Script

```
labs/lab14_02_real_time_preprocessing.py
```

---

## Input File

### Live EEG Stream

```
realtime/data/live_eeg_stream.csv
```

---

## Processing Steps

1. Load the real-time EEG stream.
2. Remove the DC offset from each EEG channel.
3. Design a fourth-order Butterworth band-pass filter.
4. Filter the EEG signals between 8 Hz and 30 Hz.
5. Save the processed EEG signals.
6. Compute descriptive statistics.
7. Generate the preprocessing report.

---

## Filter Parameters

| Parameter | Value |
|-----------|------:|
| Filter Type | Butterworth |
| Filter Order | 4 |
| Low Cutoff | 8 Hz |
| High Cutoff | 30 Hz |
| Sampling Rate | 250 Hz |

---

## Generated Files

### Preprocessed EEG Dataset

```
realtime/data/preprocessed_eeg.csv
```

### Preprocessing Report

```
realtime/results/lab14_02_preprocessing_report.txt
```

---

## Experimental Result

The preprocessing stage successfully processed the EEG stream generated in Lab 14.1.

| Metric | Value |
|---------|------:|
| Input Channels | **8** |
| Sampling Rate | **250 Hz** |
| Frequency Range | **8–30 Hz** |
| Output Samples | **1250** |

---

## Example Console Output

```
============================================================
Lab14.2 - Real-Time Preprocessing
============================================================

Original Dataset Shape

(1250, 8)

DC Offset Removed.

Band-pass Filter Applied.

Preprocessed EEG Saved Successfully.

Processed Dataset Shape

(1250, 8)

Report Saved.

Lab14.2 Finished Successfully.
```

---

## Output Dataset

The generated dataset contains the filtered EEG signals that are ready for feature extraction.

Example structure:

| EEG_1 | EEG_2 | EEG_3 | EEG_4 | EEG_5 | EEG_6 | EEG_7 | EEG_8 |
|------:|------:|------:|------:|------:|------:|------:|------:|
| ... | ... | ... | ... | ... | ... | ... | ... |

---

## Discussion

Real-time preprocessing is an essential stage in Brain–Computer Interface systems because classification performance strongly depends on signal quality.

Removing the DC offset stabilizes the baseline of each EEG channel, while the Butterworth band-pass filter suppresses unwanted low-frequency drift and high-frequency noise.

The resulting signals primarily preserve the Mu and Beta rhythms, which contain the most informative patterns for motor imagery recognition.

The generated preprocessed EEG dataset will be used directly in the following laboratory for online Common Spatial Pattern (CSP) feature extraction.

---

## Conclusion

The real-time EEG preprocessing stage was successfully implemented.

The acquired EEG stream was normalized by removing the DC offset and filtered using a fourth-order Butterworth band-pass filter between 8 Hz and 30 Hz.

The processed EEG signals were stored for subsequent real-time feature extraction, providing a clean and reliable input for the next stage of the proposed Brain–Computer Interface framework.