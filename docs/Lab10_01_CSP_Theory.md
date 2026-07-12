# Lab 10.1 – Common Spatial Patterns (CSP) Theory

## Objective

The objective of this laboratory is to introduce the Common Spatial Patterns (CSP) algorithm and train the first CSP model using EEG motor imagery data.

The trained CSP model will be used in the following laboratories to extract spatial features for machine learning classification.

---

## Background

Common Spatial Patterns (CSP) is one of the most widely used feature extraction techniques in Brain–Computer Interface (BCI) systems.

CSP learns spatial filters that maximize the variance for one class while minimizing it for another class. This enhances the discriminative information contained in EEG signals.

The extracted spatial features significantly improve the performance of classifiers such as Support Vector Machines (SVM), Random Forest, and XGBoost.

---

## Dataset

- Dataset: EEG Motor Movement / Imagery Dataset (EEGBCI)
- Subject: 1
- Run: 4

Input File

```
processed_data/subject01_run04-epo.fif
```

---

## Python Script

```
labs/lab10_01_csp_theory.py
```

---

## CSP Parameters

| Parameter | Value |
|----------|-------|
| Components | 4 |
| Log Transform | Enabled |
| Regularization | None |
| Trace Normalization | Disabled |

---

## Results

Epoch Shape

```
(X.shape)
```

Detected Classes

```
Unique Event IDs
```

Generated Model

```
csp/csp_model.pkl
```

---

## Generated Files

### CSP Model

```
csp/csp_model.pkl
```

### Report

```
results/lab10_01_csp_theory_report.txt
```

---

## Discussion

The CSP model was successfully trained using EEG motor imagery epochs.

The learned spatial filters emphasize class-specific brain activity and suppress irrelevant signal components.

The trained model will be reused to transform EEG signals into low-dimensional spatial feature vectors suitable for machine learning.

---

## Conclusion

The first CSP model was successfully created and stored.

This model represents the beginning of the spatial feature extraction stage and prepares the EEG dataset for classical machine learning algorithms in the following laboratories.