# Lab 13.3 – Online Learning

## Objective

The objective of this laboratory is to simulate the Online Learning mechanism of the proposed Adaptive Artificial Intelligence system.

Instead of updating the classifier after every prediction, the system continuously monitors the amount and quality of accumulated user feedback and determines whether sufficient new data are available to initiate model updating.

---

## Background

Online Learning enables Artificial Intelligence systems to continuously improve their performance as new data become available.

In Brain–Computer Interface (BCI) applications, user characteristics and EEG signals change over time due to fatigue, attention, learning effects, and environmental conditions.

Updating the classifier after every prediction may lead to unstable learning when only a few feedback samples are available.

Therefore, an adaptive decision mechanism is introduced to determine whether enough feedback has been collected before initiating classifier updating.

---

## Python Script

```
labs/lab13_03_online_learning.py
```

---

## Input Files

### User Feedback Database

```
adaptive_ai/user_feedback.csv
```

### Adaptive Threshold

```
adaptive_ai/adaptive_threshold.csv
```

---

## Processing Steps

1. Load the accumulated user feedback.
2. Load the adaptive confidence threshold.
3. Calculate the current feedback accuracy.
4. Count the available feedback samples.
5. Compare the sample count with the minimum requirement.
6. Decide whether online learning can begin.
7. Save the current online learning status.
8. Generate the performance report.

---

## Online Learning Decision

The system uses the following policy:

| Feedback Samples | Decision |
|-----------------:|----------|
| < 10 | WAITING |
| ≥ 10 | READY |

This strategy prevents unnecessary classifier updates when insufficient feedback data are available.

---

## Experimental Result

The execution of this laboratory produced the following results:

| Metric | Value |
|---------|------:|
| Feedback Samples | **3** |
| Feedback Accuracy | **1.00** |
| Adaptive Threshold | **0.90** |
| Status | **WAITING** |

The system requires **7 additional feedback samples** before initiating adaptive classifier updating.

---

## Generated Files

### Online Learning Status

```
adaptive_ai/online_learning_status.csv
```

### Online Learning Report

```
results/lab13_03_online_learning_report.txt
```

---

## Example Console Output

```
============================================================
Lab13.3 - Online Learning
============================================================

Feedback Samples : 3
Feedback Accuracy: 1.00
Current Threshold: 0.90

Online Learning Status
----------------------
WAITING

Collect 7 more feedback samples before updating the classifier.

Status Saved.
Report Saved.

Lab13.3 Finished Successfully.
```

---

## Discussion

This laboratory introduces an Online Learning decision mechanism for the proposed Adaptive Artificial Intelligence framework.

Rather than immediately updating the classifier after each interaction, the system evaluates whether sufficient user feedback has been accumulated to justify a model update.

This approach improves learning stability, reduces unnecessary retraining, and minimizes the risk of adapting the classifier using an insufficient amount of new data.

The generated status file will be used in the following laboratory to determine when adaptive classifier updating should be performed.

---

## Conclusion

An Online Learning decision mechanism was successfully implemented.

The system automatically analyzed the available user feedback, evaluated the current adaptive threshold, and determined whether enough feedback samples had been collected for classifier updating.

The generated status information provides the foundation for the adaptive classifier update process implemented in the next laboratory.