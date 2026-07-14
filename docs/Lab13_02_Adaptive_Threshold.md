# Lab 13.2 – Adaptive Confidence Threshold

## Objective

The objective of this laboratory is to dynamically adjust the confidence threshold of the Adaptive Artificial Intelligence system based on accumulated user feedback.

Instead of using a fixed confidence threshold, the system continuously analyzes previous user interactions and automatically updates the decision threshold according to its observed performance.

---

## Background

Conventional Brain–Computer Interface (BCI) systems typically operate with a fixed confidence threshold throughout their lifetime.

However, EEG signal characteristics vary over time due to user fatigue, attention level, emotional state, and environmental conditions.

Adaptive Artificial Intelligence addresses this limitation by continuously monitoring user feedback and modifying the confidence threshold whenever the system performance changes.

This adaptive strategy improves the robustness and reliability of long-term BCI operation.

---

## Python Script

```
labs/lab13_02_adaptive_threshold.py
```

---

## Input Files

### User Feedback Database

```
adaptive_ai/user_feedback.csv
```

---

## Processing Steps

1. Load the accumulated user feedback database.
2. Count the total number of feedback samples.
3. Calculate the current feedback accuracy.
4. Determine the appropriate confidence threshold.
5. Save the updated adaptive threshold.
6. Display the adaptive statistics.

---

## Adaptive Threshold Strategy

The threshold is updated according to the following rules:

| Feedback Accuracy | Adaptive Threshold |
|------------------:|-------------------:|
| ≥ 90% | 0.90 |
| ≥ 75% | 0.85 |
| ≥ 60% | 0.80 |
| < 60% | 0.70 |

This strategy allows the classifier to become more conservative when its performance is high and more tolerant when performance decreases.

---

## Experimental Result

The execution of this laboratory produced the following results:

| Metric | Value |
|---------|------:|
| Feedback Samples | **3** |
| Feedback Accuracy | **1.00** |
| Adaptive Threshold | **0.90** |

---

## Generated Files

### Adaptive Threshold Database

```
adaptive_ai/adaptive_threshold.csv
```

---

## Example Output

```
============================================================
Lab13.2 - Adaptive Confidence Threshold
============================================================

Feedback Records : 3

Current Feedback Accuracy : 1.00

New Adaptive Threshold : 0.90

Adaptive Threshold Saved Successfully.

Lab13.2 Finished Successfully.
```

---

## Discussion

The adaptive threshold mechanism enables the proposed BCI system to continuously modify its decision confidence according to accumulated user feedback.

As additional feedback is collected, the threshold automatically reflects the observed prediction quality.

This adaptive mechanism represents the first stage of self-adjustment within the proposed Adaptive Artificial Intelligence framework and prepares the system for continuous online learning.

---

## Conclusion

The adaptive confidence threshold mechanism was successfully implemented.

The system automatically analyzed user feedback, calculated the current performance, and generated an updated confidence threshold.

The resulting adaptive threshold will be used in the next laboratory to support online learning and continuous model adaptation.