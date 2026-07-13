# Lab 12.7 – Save Best Deep Learning Model

## Objective

The objective of this laboratory is to automatically identify, save, and document the best-performing Deep Learning classifier developed in Chapter 12.

The selected model represents the final Deep Learning classifier that will be used in the subsequent stages of the proposed Hybrid Adaptive Brain–Computer Interface (BCI) system.

---

## Background

Several Deep Learning models were developed and evaluated throughout Chapter 12.

These models include:

- Convolutional Neural Network (CNN)
- Long Short-Term Memory (LSTM)
- CNN–LSTM Hybrid

Selecting the best-performing model based on objective evaluation metrics ensures that the most reliable classifier is used for future real-time implementation and adaptive learning.

---

## Python Script

```
labs/lab12_07_save_best_model.py
```

---

## Input Files

### Performance Comparison

```
results/lab12_05_model_comparison.csv
```

### Candidate Models

```
deep_learning/cnn_classifier.keras

deep_learning/lstm_classifier.keras

deep_learning/cnn_lstm_classifier.keras
```

---

## Processing Steps

1. Load the Deep Learning comparison table.
2. Read the evaluation metrics.
3. Determine the best-performing model according to classification accuracy.
4. Copy the selected model to the final deployment directory.
5. Generate the final model report.
6. Display the selected model information.

---

## Model Selection Strategy

The best model is selected using the following criteria:

1. Highest Accuracy
2. Precision
3. Recall
4. F1-Score

Accuracy is used as the primary decision criterion, while the remaining metrics provide additional validation of classifier performance.

---

## Experimental Result

The execution of this laboratory selected the following Deep Learning model:

| Metric | Value |
|---------|------:|
| Selected Model | **CNN** |
| Accuracy | **1.0000** |
| Precision | **1.0000** |
| Recall | **1.0000** |
| F1 Score | **1.0000** |

---

## Generated Files

### Final Deep Learning Model

```
models/final_deep_learning_model.keras
```

### Final Evaluation Report

```
results/lab12_07_final_model_report.txt
```

---

## Console Output

```
============================================================
Deep Learning Final Model
============================================================

Model     : CNN
Accuracy  : 1.0000
Precision : 1.0000
Recall    : 1.0000
F1 Score  : 1.0000

Model Saved To:
models/final_deep_learning_model.keras
```

---

## Discussion

The comparison of all developed Deep Learning classifiers identified the CNN model as the highest-performing architecture for the current EEG motor imagery dataset.

Although the CNN model achieved perfect classification accuracy on the available testing dataset, it is important to note that the dataset contains a relatively limited number of training and testing samples.

Consequently, the reported performance reflects the current experimental dataset and should be validated using larger datasets in future work to assess the model's generalization capability.

The selected CNN classifier will serve as the final Deep Learning model for the proposed Hybrid Adaptive Brain–Computer Interface system.

---

## Conclusion

The best-performing Deep Learning model was successfully identified, documented, and saved.

The final deployment model was copied to the project's model directory and accompanied by a detailed evaluation report.

This laboratory completes Chapter 12 and provides the final Deep Learning classifier for subsequent adaptive learning, real-time BCI implementation, and robotic control experiments presented in the following chapters.