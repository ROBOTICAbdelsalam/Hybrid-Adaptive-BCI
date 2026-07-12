# Lab 11.4 – Support Vector Machine (SVM) Classifier

## Objective

The objective of this laboratory is to train and evaluate a Support Vector Machine (SVM) classifier using the extracted Common Spatial Patterns (CSP) features.

The trained classifier is evaluated using multiple performance metrics to assess its ability to classify EEG motor imagery signals.

---

## Background

Support Vector Machine (SVM) is one of the most widely used machine learning algorithms in Brain–Computer Interface (BCI) research.

SVM constructs an optimal decision boundary that maximizes the separation between different classes in the feature space.

Due to its robustness and strong generalization capability, SVM is considered a standard baseline classifier for EEG classification.

---

## Input Files

### Training Data

```
ml_data/X_train.csv
ml_data/y_train.csv
```

### Testing Data

```
ml_data/X_test.csv
ml_data/y_test.csv
```

---

## Python Script

```
labs/lab11_04_svm_classifier.py
```

---

## Processing Steps

1. Load the training and testing datasets.
2. Initialize the SVM classifier using the RBF kernel.
3. Train the classifier using the training dataset.
4. Predict class labels for the testing dataset.
5. Compute classification performance metrics.
6. Generate the confusion matrix.
7. Save the trained model.
8. Generate the evaluation report.

---

## Generated Files

### Trained Model

```
models/svm_classifier.pkl
```

### Evaluation Report

```
results/lab11_04_svm_report.txt
```

### Confusion Matrix

```
figures/lab11_svm_confusion_matrix.png
```

### Documentation Figure

```
docs/images/lab11_svm_confusion_matrix.png
```

---

## Performance Metrics

The following metrics were calculated:

- Accuracy
- Precision
- Recall
- F1-Score

Experimental Results:

| Metric | Value |
|--------|-------|
| Accuracy | **83.33%** |
| Precision | **70.83%** |
| Recall | **83.33%** |
| F1-Score | **76.19%** |

---

## Figure

![SVM Confusion Matrix](images/lab11_svm_confusion_matrix.png)

**Figure 11.1** Confusion matrix of the Support Vector Machine (SVM) classifier.

---

## Discussion

The SVM classifier successfully classified the CSP feature vectors and achieved promising performance despite the relatively small dataset.

The confusion matrix provides insight into correctly classified samples and classification errors.

These results establish a strong baseline for comparison with additional classifiers such as Random Forest and XGBoost.

---

## Conclusion

The Support Vector Machine classifier was successfully trained and evaluated.

The trained model achieved satisfactory classification performance and was saved for future inference and comparative evaluation.

The next laboratory will investigate the performance of a Random Forest classifier using the same training and testing datasets.
