# Lab 13.1 – User Feedback Integration

## Objective

The objective of this laboratory is to introduce user feedback into the proposed Adaptive Artificial Intelligence framework.

The system records the user's evaluation of each predicted command, creating a continuously growing feedback database that will later be used for adaptive learning and model improvement.

---

## Background

Traditional Brain–Computer Interface (BCI) systems usually rely on a fixed classification model that does not change after deployment.

However, user behavior and EEG signals naturally vary over time due to fatigue, attention, emotional state, and environmental conditions.

To overcome this limitation, Adaptive Artificial Intelligence incorporates user feedback into the learning process.

This enables the system to monitor its prediction quality and gradually improve its future performance.

---

## Python Script

```
labs/lab13_01_user_feedback.py
```

---

## Input

### Simulated Prediction

```
Predicted Command

Confidence Score
```

### User Feedback

```
yes

or

no
```

---

## Processing Steps

1. Simulate a predicted command.
2. Display the confidence score.
3. Request feedback from the user.
4. Determine whether the prediction is correct.
5. Store the interaction in the feedback database.
6. Display the updated feedback history.

---

## Feedback Database

The feedback information is stored in:

```
adaptive_ai/user_feedback.csv
```

Each execution appends a new record instead of overwriting previous data.

---

## Stored Information

Each feedback record contains:

- Timestamp
- Predicted Command
- Confidence Score
- User Feedback
- Correct Prediction Flag

---

## Example Output

| Timestamp | Predicted Command | Confidence | User Feedback | Correct |
|-----------|-------------------|-----------:|---------------|---------|
| 2026-07-14 01:32:59 | Move Left | 0.87 | yes | True |

---

## Console Output

```
============================================================
Lab13.1 - User Feedback Integration
============================================================

Predicted Command : Move Left
Confidence        : 0.87

Was the prediction correct? (yes/no): yes

Feedback Saved Successfully.

Lab13.1 Finished Successfully.
```

---

## Generated Files

### Feedback Database

```
adaptive_ai/user_feedback.csv
```

---

## Discussion

This laboratory introduces the first adaptive component of the proposed Brain–Computer Interface system.

Instead of treating each prediction independently, the system stores user feedback after every interaction.

The accumulated feedback database provides valuable information for future adaptive algorithms, including threshold adjustment, online learning, and classifier updating.

This feedback mechanism enables the system to gradually learn from user experience rather than relying solely on its initial training.

---

## Conclusion

The user feedback integration mechanism was successfully implemented.

A structured feedback database was created to store user evaluations together with prediction confidence and timestamps.

The generated dataset establishes the foundation for adaptive learning in the following laboratories, where the classifier will dynamically improve its behavior based on accumulated user interactions.