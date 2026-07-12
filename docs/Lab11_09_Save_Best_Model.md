# Lab 11.9 – Save Best Model

## Objective

The objective of this laboratory is to select, save, and prepare the final machine learning model for deployment within the proposed Hybrid Adaptive Brain–Computer Interface (BCI) system.

The selected model will be used in the subsequent stages of the project for real-time EEG signal classification and robotic control.

---

## Background

After evaluating several machine learning classifiers, the final model must be stored in a standardized format for future inference and deployment.

Saving the trained model eliminates the need for retraining each time the system is executed and enables seamless integration with the real-time BCI pipeline.

In addition to the trained model, metadata describing the model configuration and performance are also preserved.

---

## Python Script

```
labs/lab11_09_save_best_model.py
```

---

## Input Files

### Trained Model

```
models/svm_classifier.pkl
```

### Optional Label Encoder

```
models/xgboost_label_encoder.pkl
```

---

## Processing Steps

1. Create the deployment directory.
2. Select the final classifier.
3. Copy the trained model.
4. Copy the label encoder (if available).
5. Generate model metadata.
6. Save the metadata.
7. Generate the final deployment report.

---

## Generated Files

### Final Model

```
final_model/final_bci_model.pkl
```

### Label Encoder

```
final_model/label_encoder.pkl
```

### Model Metadata

```
final_model/model_information.pkl
```

### Final Report

```
results/lab11_09_final_model_report.txt
```

---

## Selected Model

The Support Vector Machine (SVM) classifier was selected as the final deployment model.

Experimental Performance:

| Metric | Value |
|---------|-------|
| Accuracy | **83.33%** |
| Precision | **70.83%** |
| Recall | **83.33%** |
| F1-Score | **76.19%** |

---

## Model Metadata

The following information is stored together with the trained model:

- Selected classifier
- Dataset
- Feature extraction method
- Accuracy
- Precision
- Recall
- F1-Score

This metadata allows the trained model to be identified and reproduced in future experiments.

---

## Discussion

Both the Support Vector Machine (SVM) and XGBoost classifiers achieved identical classification performance on the current EEG dataset.

For deployment in this project, the Support Vector Machine model was selected because of its simplicity, computational efficiency, and ease of integration with the proposed Hybrid Adaptive BCI architecture.

The final deployment package contains all files required for future inference without retraining the classifier.

---

## Conclusion

The final machine learning model was successfully prepared for deployment.

The trained classifier, metadata, deployment package, and evaluation report were successfully generated and organized.

This completes the machine learning stage of the proposed Hybrid Adaptive Brain–Computer Interface project and prepares the system for integration with ROS2 and the real-time EEG processing pipeline.

---

## Chapter 11 Summary

The following laboratories were successfully completed:

- Lab11.1 – Dataset Preparation
- Lab11.2 – Create Labels
- Lab11.3 – Train/Test Split
- Lab11.4 – Support Vector Machine (SVM)
- Lab11.5 – Random Forest
- Lab11.6 – XGBoost
- Lab11.7 – Model Comparison
- Lab11.8 – Performance Evaluation
- Lab11.9 – Save Best Model

Chapter 11 establishes a complete machine learning pipeline for EEG motor imagery classification, beginning with dataset preparation and ending with a deployable trained model ready for integration into the Hybrid Adaptive Brain–Computer Interface system.