# Lab 10.5 – Save CSP Features

## Objective

The objective of this laboratory is to validate, organize, and save the extracted Common Spatial Patterns (CSP) features into a final dataset that will be used in subsequent machine learning experiments.

This step ensures that the CSP feature matrix is complete, free of missing values, and ready for classification.

---

## Background

After extracting spatial features using the Common Spatial Patterns (CSP) algorithm, the resulting feature matrix must be verified before training machine learning models.

The validation process includes:

- Checking the number of samples.
- Checking the number of extracted features.
- Detecting missing values.
- Saving the final CSP dataset.

This guarantees data consistency and reproducibility.

---

## Input Dataset

```
csp/csp_features.csv
```

---

## Python Script

```
labs/lab10_05_save_csp_features.py
```

---

## Processing Steps

1. Load the CSP feature matrix.
2. Verify the dataset dimensions.
3. Detect missing values.
4. Save the validated CSP dataset.
5. Generate a dataset summary.
6. Generate a processing report.

---

## Generated Files

### Final CSP Dataset

```
csp/csp_dataset.csv
```

### Dataset Summary

```
results/lab10_05_csp_dataset_summary.csv
```

### Report

```
results/lab10_05_save_csp_features_report.txt
```

---

## Validation Results

The following checks were performed:

- Number of samples
- Number of CSP features
- Missing value detection

The generated dataset is complete and suitable for machine learning.

---

## Discussion

The validation process confirmed that the CSP feature matrix is structurally consistent and contains no missing values.

Preparing a validated dataset before classifier training improves reproducibility and reduces the likelihood of errors during the machine learning stage.

---

## Conclusion

The CSP feature dataset was successfully validated and saved.

The resulting dataset represents the final spatial feature matrix that will be used as the input for the machine learning models developed in the next chapter.