# Lab 12.6 – Performance Evaluation

## Objective

The objective of this laboratory is to perform a comprehensive evaluation of the Deep Learning models developed in Chapter 12 and identify the best-performing classifier based on multiple performance metrics.

This evaluation provides the final assessment before selecting the optimal Deep Learning model for deployment in the proposed Hybrid Adaptive Brain–Computer Interface (BCI) system.

---

## Background

Performance evaluation is a critical stage in machine learning and deep learning research.

Although different models may achieve similar classification accuracy, additional evaluation metrics are required to assess their reliability and robustness.

Therefore, this laboratory evaluates each Deep Learning model using multiple statistical measures and selects the model that demonstrates the best overall performance.

---

## Python Script

```
labs/lab12_06_performance_evaluation.py
```

---

## Input Files

```
results/lab12_05_model_comparison.csv
```

---

## Processing Steps

1. Load the Deep Learning model comparison table.
2. Read the evaluation metrics for all classifiers.
3. Identify the best-performing model.
4. Display the evaluation summary.
5. Generate the final performance report.
6. Save the evaluation results.

---

## Evaluated Models

- CNN
- LSTM
- CNN-LSTM Hybrid

---

## Evaluation Metrics

The following metrics are analyzed:

- Accuracy
- Precision
- Recall
- F1-Score

---

## Performance Selection

The best model is selected according to the highest classification accuracy.

When two models obtain similar accuracy values, Precision, Recall, and F1-Score are also considered to support the final evaluation.

---

## Generated Files

### Final Performance Report

```
results/lab12_06_performance_report.txt
```

---

## Performance Summary

The generated report contains:

- Best Deep Learning model
- Accuracy
- Precision
- Recall
- F1-Score

The numerical values are automatically extracted from the comparison table generated in Lab 12.5.

---

## Discussion

The performance evaluation provides an objective comparison of all developed Deep Learning classifiers.

By analyzing multiple evaluation metrics rather than relying solely on accuracy, a more reliable assessment of classifier performance can be achieved.

The selected model represents the most suitable Deep Learning architecture for the proposed EEG motor imagery classification framework and will be used in the final deployment stage.

---

## Conclusion

The Deep Learning models were successfully evaluated using multiple statistical performance measures.

The best-performing classifier was automatically identified and documented.

The generated evaluation report provides the basis for selecting the final Deep Learning model, which will be saved and prepared for integration in the next laboratory.