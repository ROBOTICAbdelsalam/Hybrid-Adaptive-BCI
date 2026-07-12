# Lab 11.3 – Train/Test Split

## Objective

The objective of this laboratory is to divide the labeled CSP dataset into training and testing subsets for supervised machine learning.

A reproducible train/test split ensures fair evaluation of classification models.

---

## Background

Machine learning models must be trained on one subset of data and evaluated on another unseen subset.

This prevents overfitting and provides an unbiased estimate of model performance.

The dataset was divided using stratified sampling to preserve the class distribution.

---

## Input Dataset

```
csp/csp_dataset_with_labels.csv
```

---

## Python Script

```
labs/lab11_03_train_test_split.py
```

---

## Processing Steps

1. Load the labeled CSP dataset.
2. Separate features and labels.
3. Apply an 80/20 train/test split.
4. Preserve class distribution using stratification.
5. Save the generated datasets.
6. Generate a processing report.

---

## Generated Files

### Training Dataset

```
ml_data/X_train.csv
ml_data/y_train.csv
```

### Testing Dataset

```
ml_data/X_test.csv
ml_data/y_test.csv
```

### Report

```
results/lab11_03_train_test_split_report.txt
```

---

## Results

The CSP dataset was successfully divided into training and testing subsets.

The generated datasets are ready for supervised machine learning experiments.

---

## Discussion

Using stratified train/test splitting preserves the class balance and improves the reliability of model evaluation.

The generated datasets will be used in the following laboratories to train and evaluate different classification algorithms.

---

## Conclusion

The dataset was successfully divided into training and testing subsets.

The project is now ready to train the first machine learning classifier.