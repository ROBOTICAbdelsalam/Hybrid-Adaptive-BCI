
# Lab 08.6 – Save Processed Epochs

## Objective

The objective of this laboratory is to save the processed EEG epochs into the native MNE FIF format for future analysis without repeating the preprocessing pipeline.

---

## Background

Repeated preprocessing increases computation time and introduces unnecessary complexity.

Saving processed epochs allows the same dataset to be reused directly for feature extraction, machine learning, deep learning, and Brain–Computer Interface (BCI) experiments.

The FIF format preserves all metadata, channel information, event annotations, and processed EEG signals.

---

## Dataset

- Dataset: EEG Motor Movement/Imagery Dataset (EEGBCI)
- Subject: 1
- Run: 4

---

## Python Script

```
labs/lab08_06_save_processed_epochs.py
```

---

## Output File

```
processed_data/subject01_run04-epo.fif
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
results/lab08_06_save_processed_epochs_report.txt
```

### Saved Dataset

```
processed_data/subject01_run04-epo.fif
```

---

## Discussion

The processed EEG epochs were successfully stored using the MNE FIF format.

This format maintains all signal information and metadata required for future analysis.

Using saved epochs significantly reduces preprocessing time during feature extraction and classifier development.

---

## Conclusion

The processed EEG epochs were successfully saved and are now available for subsequent laboratories, including feature extraction, spatial filtering, machine learning, and deep learning.