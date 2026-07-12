# Lab 11.8 – Performance Evaluation

## Objective

The objective of this laboratory is to evaluate the overall performance of the developed machine learning pipeline for EEG motor imagery classification.

This laboratory summarizes the performance of all implemented classifiers and identifies the most suitable model for the proposed Hybrid Adaptive Brain–Computer Interface (BCI) system.

---

## Background

Performance evaluation is an essential stage in every machine learning pipeline.

Rather than evaluating a single classifier, this laboratory compares all trained models using the same evaluation metrics and dataset.

The evaluation provides an objective assessment of each classifier and supports the selection of the most appropriate model for future deployment.

---

## Python Script

```
labs/lab11_08_performance_evaluation.py
```

---

## Input File

```
results/lab11_07_model_comparison.csv
```

---

## Evaluation Metrics

The following performance metrics were analyzed:

- Accuracy
- Precision
- Recall
- F1-Score

Average values were also computed across all evaluated models.

---

## Compared Models

- Support Vector Machine (SVM)
- Random Forest
- XGBoost

---

## Experimental Results

| Model | Accuracy | Precision | Recall | F1-Score |
|--------|---------:|----------:|-------:|---------:|
| Support Vector Machine | **83.33%** | **70.83%** | **83.33%** | **76.19%** |
| Random Forest | **66.67%** | **66.67%** | **66.67%** | **66.67%** |
| XGBoost | **83.33%** | **70.83%** | **83.33%** | **76.19%** |

---

## Average Performance

| Metric | Average |
|---------|---------:|
| Accuracy | **77.78%** |
| Precision | **69.44%** |
| Recall | **77.78%** |
| F1-Score | **73.02%** |

---

## Generated File

### Performance Report

```
results/lab11_08_performance_evaluation_report.txt
```

---

## Performance Analysis

The evaluation demonstrates that both the Support Vector Machine (SVM) and XGBoost classifiers achieved the highest classification performance on the current EEG dataset.

Random Forest produced lower classification accuracy and lower overall performance compared with the other classifiers.

The average evaluation metrics indicate that the developed machine learning pipeline provides reliable classification performance despite the relatively small number of EEG trials.

---

## Discussion

The obtained results are consistent with many Brain–Computer Interface studies where Support Vector Machine and gradient boosting algorithms outperform ensemble tree methods when limited training samples are available.

Although SVM and XGBoost achieved identical performance in the current experiments, XGBoost offers additional flexibility for larger datasets, while SVM remains computationally efficient and easy to optimize.

These findings suggest that either classifier can be successfully integrated into the proposed Hybrid Adaptive BCI system.

---

## Conclusion

The performance evaluation successfully compared all developed machine learning models.

Both Support Vector Machine (SVM) and XGBoost achieved the highest overall performance, while Random Forest demonstrated lower classification capability on the current dataset.

The obtained evaluation confirms the effectiveness of the CSP feature extraction pipeline and validates the proposed machine learning framework for EEG motor imagery classification.

The next laboratory will save the final selected model and prepare it for deployment within the Hybrid Adaptive Brain–Computer Interface system.