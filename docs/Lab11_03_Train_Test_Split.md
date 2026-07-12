# Lab 11.2 – Create Labels

## Objective

The objective of this laboratory is to generate class labels for the Common Spatial Patterns (CSP) feature dataset using the processed EEG epochs.

The generated labels will be appended to the CSP feature matrix, producing a complete dataset suitable for supervised machine learning algorithms.

---

## Background

Machine learning classifiers require both feature vectors and corresponding class labels.

The labels are extracted from the processed EEG epochs generated during the epoching stage.

Each CSP feature vector is associated with one EEG epoch and receives its corresponding class label.

---

## Input Files

```
csp/csp_dataset.csv

processed_data/subject01_run04-epo.fif
```

---

## Python Script

```
labs/lab11_02_create_labels.py
```

---

## Processing Steps

1. Load the CSP feature dataset.
2. Load the processed EEG epochs.
3. Extract event labels.
4. Verify feature-label consistency.
5. Append labels to the dataset.
6. Save the labeled dataset.
7. Generate a processing report.

---

## Output Files

### Dataset with Labels

```
csp/csp_dataset_with_labels.csv
```

### Report

```
results/lab11_02_create_labels_report.txt
```

---

## Results

The CSP feature matrix was successfully combined with the corresponding EEG class labels.

The resulting dataset contains:

- CSP Features
- Class Labels

This dataset is now ready for supervised machine learning.

---

## Discussion

Correct alignment between features and labels is essential for reliable classifier training.

The validation step ensured that the number of feature vectors exactly matched the number of EEG epochs.

---

## Conclusion

The labeled CSP dataset was successfully generated.

The project is now ready for train/test splitting and machine learning classification.