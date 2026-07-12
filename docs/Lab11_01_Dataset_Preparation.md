# Lab 11.1 – Dataset Preparation

## Objective

The objective of this laboratory is to prepare the Common Spatial Patterns (CSP) dataset for machine learning classification.

This includes loading the dataset, validating its integrity, checking for missing values, and generating a summary report.

---

## Background

Before training machine learning models, the input dataset must be verified to ensure consistency and completeness.

Dataset preparation is an essential preprocessing step that guarantees reliable model training and evaluation.

---

## Input Dataset

```
csp/csp_dataset.csv
```

---

## Python Script

```
labs/lab11_01_dataset_preparation.py
```

---

## Processing Steps

1. Load the CSP dataset.
2. Count the number of samples.
3. Count the number of features.
4. Check for missing values.
5. Display data types.
6. Generate a preparation report.

---

## Generated File

### Report

```
results/lab11_01_dataset_preparation_report.txt
```

---

## Results

The dataset was successfully loaded and validated.

The report contains:

- Number of samples
- Number of features
- Missing values
- Dataset column names

The dataset is now ready for machine learning preprocessing.

---

## Discussion

Dataset validation ensures that no missing values or structural inconsistencies exist before model training.

Performing this verification step improves reproducibility and minimizes potential training errors.

---

## Conclusion

The CSP dataset was successfully prepared and validated.

The project is now ready to perform train/test splitting and begin machine learning model development.