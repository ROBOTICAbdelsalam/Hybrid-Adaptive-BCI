# Lab 08.4 – Epoch Visualization

## Objective

The objective of this laboratory is to visualize the averaged EEG epochs after preprocessing and baseline correction. Visual inspection is an essential step for evaluating signal quality before feature extraction and classification.

---

## Background

Visualization allows researchers to verify that EEG preprocessing has been successfully completed and that the averaged brain responses are consistent across trials.

The averaged response (Evoked Response) is calculated by averaging all valid epochs belonging to the experiment.

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
labs/lab08_04_epoch_visualization.py
```

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

---

## Generated Files

### Report

```
results/lab08_04_epoch_visualization_report.txt
```

### Figure

```
figures/lab08_epoch_visualization.png
```

---

## Figure

![Epoch Visualization](images/lab08_epoch_visualization.png)

**Figure 1.** Average EEG response across all valid epochs.

---

## Discussion

Visual inspection confirms that the preprocessing pipeline successfully generated clean EEG epochs suitable for further analysis.

The averaged response provides an overview of brain activity and helps identify abnormal recordings before feature extraction.

---

## Conclusion

Epoch visualization was successfully completed. The generated figure confirms that the EEG epochs are correctly aligned and ready for quality assessment and feature extraction.