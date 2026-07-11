# Lab 08.3 – Baseline Correction

## Objective

The objective of this laboratory is to apply baseline correction to EEG epochs in order to remove constant offsets and improve signal quality before feature extraction and classification.

---

## Background

Baseline correction is one of the most important preprocessing steps in EEG signal analysis.

Each EEG epoch may contain a small DC offset caused by electrodes, amplifiers, or environmental noise. This offset can negatively affect statistical analysis and machine learning performance.

Baseline correction removes this offset by subtracting the average signal value calculated from the baseline interval before the event.

---

## Dataset

- Dataset: EEG Motor Movement/Imagery Dataset (EEGBCI)
- Subject: 1
- Run: 4
- Channels: 64 EEG
- Sampling Frequency: 160 Hz

---

## Python Script

```
labs/lab08_03_baseline_correction.py
```

---

## Baseline Parameters

| Parameter | Value |
|-----------|-------|
| Baseline Interval | -0.2 s to 0.0 s |
| tmin | -0.2 s |
| tmax | 0.8 s |

---

## Processing Steps

1. Load the EEG dataset.
2. Extract event markers.
3. Create EEG epochs.
4. Apply baseline correction.
5. Verify the corrected epochs.
6. Save the processing report.
7. Generate an average epoch figure.
8. Copy the figure into the documentation folder.

---

## Results

Detected Events

```
30
```

Valid Epochs

```
29
```

Epoch Shape

```
(29, 64, 161)
```

One epoch was automatically discarded because insufficient EEG samples existed before the first event.

---

## Generated Files

### Python Script

```
labs/lab08_03_baseline_correction.py
```

### Report

```
results/lab08_03_baseline_correction_report.txt
```

### Figure

```
figures/lab08_baseline_correction.png
```

---

## Figure

![Baseline Correction](images/lab08_baseline_correction.png)

**Figure 1.** Average EEG response after applying baseline correction.

---

## Discussion

Baseline correction removes slow DC offsets from each EEG epoch using the mean signal value measured before the experimental event.

This process improves signal consistency across all trials and provides cleaner data for subsequent feature extraction and machine learning algorithms.

Proper baseline correction is essential because it reduces variability that is unrelated to brain activity.

---

## Conclusion

Baseline correction was successfully applied to all valid EEG epochs.

The corrected EEG data are now ready for visualization, quality assessment, feature extraction, and classification in the following laboratories.