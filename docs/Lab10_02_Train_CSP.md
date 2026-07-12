# Lab 10.2 – Train Common Spatial Patterns (CSP)

## Objective

The objective of this laboratory is to apply the previously trained Common Spatial Patterns (CSP) model to the EEG epochs and transform them into low-dimensional spatial feature vectors.

These features will be used as input for classical machine learning algorithms in the next chapter.

---

## Background

Common Spatial Patterns (CSP) is a supervised feature extraction technique that learns spatial filters maximizing variance differences between EEG classes.

After training, the CSP model can transform each EEG epoch into a compact feature vector containing the most discriminative spatial information.

These features are commonly used with:

- Support Vector Machine (SVM)
- Random Forest
- Logistic Regression
- K-Nearest Neighbors (KNN)
- XGBoost

---

## Dataset

- Dataset: EEG Motor Movement / Imagery Dataset (EEGBCI)
- Subject: 1
- Run: 4

Input Files

```
processed_data/subject01_run04-epo.fif
csp/csp_model.pkl
```

---

## Python Script

```
labs/lab10_02_train_csp.py
```

---

## Processing Steps

1. Load EEG epochs.
2. Load the trained CSP model.
3. Apply CSP transformation.
4. Generate spatial feature vectors.
5. Save the extracted features.

---

## Results

Original EEG Shape

```
(X.shape)
```

CSP Feature Shape

```
(X_csp.shape)
```

Output File

```
csp/csp_features.csv
```

---

## Generated Files

### CSP Features

```
csp/csp_features.csv
```

### Report

```
results/lab10_02_train_csp_report.txt
```

---

## Discussion

The CSP transformation reduced the dimensionality of the EEG data while preserving the spatial information most relevant for classification.

Compared with raw EEG signals, CSP features are more compact and discriminative, making them suitable for machine learning classifiers.

---

## Conclusion

The trained CSP model successfully transformed the EEG epochs into spatial feature vectors.

The generated CSP feature matrix will be used in the following laboratories for visualization, validation, and machine learning classification.
