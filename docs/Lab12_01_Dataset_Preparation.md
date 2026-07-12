# Lab 12.1 – Deep Learning Dataset Preparation

## Objective

The objective of this laboratory is to prepare the EEG motor imagery dataset for Deep Learning models.

The dataset generated in Chapter 11 is converted into a format suitable for Convolutional Neural Networks (CNN), Long Short-Term Memory (LSTM), and hybrid CNN-LSTM architectures.

---

## Background

Deep Learning models require input data in multidimensional tensor format rather than traditional two-dimensional feature matrices.

Therefore, the CSP feature dataset generated during the Machine Learning stage is reshaped and encoded before training Deep Learning models.

This laboratory serves as the foundation for all Deep Learning experiments in Chapter 12.

---

## Python Script

```
labs/lab12_01_dataset_preparation.py
```

---

## Input Files

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

---

## Processing Steps

1. Load the Machine Learning training and testing datasets.
2. Encode class labels using LabelEncoder.
3. Reshape the feature matrices into three-dimensional tensors.
4. Save the prepared datasets in NumPy format.
5. Save the trained LabelEncoder.
6. Generate a preparation report.

---

## Dataset Transformation

Original Machine Learning format:

```
(Number of Samples, Number of Features)
```

Example:

```
(23, 4)
```

Deep Learning format:

```
(Number of Samples, Number of Features, Channels)
```

Example:

```
(23, 4, 1)
```

The additional dimension represents the input channel required by neural network layers.

---

## Generated Files

### Deep Learning Dataset

```
dl_data/X_train.npy
dl_data/X_test.npy
dl_data/y_train.npy
dl_data/y_test.npy
```

### Label Encoder

```
dl_data/label_encoder.pkl
```

### Report

```
results/lab12_01_dataset_preparation_report.txt
```

---

## Output Summary

Training Samples

```
23
```

Testing Samples

```
6
```

Training Shape

```
(23, 4, 1)
```

Testing Shape

```
(6, 4, 1)
```

Number of Classes

```
3
```

---

## Discussion

The EEG dataset was successfully transformed into a tensor representation suitable for Deep Learning models.

Class labels were encoded into numerical values while preserving their original mapping through a LabelEncoder.

The prepared dataset can now be directly used for CNN, LSTM, and CNN-LSTM models without additional preprocessing.

---

## Conclusion

The dataset preparation process was successfully completed.

All Deep Learning datasets, label encodings, and reports were generated successfully.

The prepared dataset will be used throughout Chapter 12 for developing and evaluating Deep Learning classifiers for EEG motor imagery recognition.