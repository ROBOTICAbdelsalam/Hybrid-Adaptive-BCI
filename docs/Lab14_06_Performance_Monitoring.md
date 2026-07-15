# Lab 14.6 – Real-Time System Evaluation

## Objective

The objective of this laboratory is to evaluate the overall performance of the real-time Hybrid Adaptive Brain–Computer Interface (BCI) system.

This evaluation summarizes the prediction performance, command execution statistics, and confidence measurements generated during online operation.

The collected metrics provide quantitative evidence of the system's reliability before deployment in robotic applications.

---

## Background

After the prediction and decision-making stages, it is essential to evaluate the overall system performance.

Performance monitoring enables researchers to determine:

- How many EEG windows were processed.
- How many commands were successfully executed.
- How many uncertain commands were rejected.
- The average confidence produced by the deep learning model.
- The execution efficiency of the BCI system.

These measurements provide an objective assessment of system reliability and support future optimization.

---

## Python Script

```
labs/lab14_06_performance_monitoring.py
```

---

## Input File

### Generated Commands

```
realtime/results/realtime_commands.csv
```

---

## Performance Metrics

The following performance indicators are calculated:

| Metric | Description |
|---------|-------------|
| Total Predictions | Number of processed EEG windows |
| Executed Commands | Commands accepted after confidence verification |
| Rejected Commands | Commands rejected as NO ACTION |
| Execution Rate | Percentage of executed commands |
| Average Confidence | Mean confidence value |
| Maximum Confidence | Highest prediction confidence |
| Minimum Confidence | Lowest prediction confidence |

---

## Processing Pipeline

1. Load generated commands.
2. Count processed EEG windows.
3. Count executed commands.
4. Count rejected commands.
5. Calculate execution rate.
6. Compute confidence statistics.
7. Save performance summary.
8. Generate performance report.

---

## Output Files

### Performance Summary

```
realtime/results/lab14_06_performance_summary.csv
```

### Performance Report

```
realtime/results/lab14_06_performance_report.txt
```

---

## Example Console Output

```
============================================================
Lab14.6 - Real-Time System Evaluation
============================================================

Performance Summary

Metric                    Value

Total Predictions            5
Executed Commands            3
Rejected Commands            2
Execution Rate (%)        60.00
Average Confidence       0.7450
Maximum Confidence       0.7646
Minimum Confidence       0.7213

Performance Summary Saved.
Performance Report Saved.

Lab14.6 Finished Successfully.
```

---

## Example Performance Table

| Metric | Value |
|---------|------:|
| Total Predictions | 5 |
| Executed Commands | 3 |
| Rejected Commands | 2 |
| Execution Rate (%) | 60.00 |
| Average Confidence | 0.7450 |
| Maximum Confidence | 0.7646 |
| Minimum Confidence | 0.7213 |

---

## Discussion

The real-time performance evaluation demonstrates that the Hybrid Adaptive BCI system successfully processed multiple EEG windows while maintaining stable prediction confidence.

A confidence threshold was applied before command execution, resulting in three accepted commands and two rejected commands.

The calculated execution rate reflects the proportion of predictions considered sufficiently reliable for robot control.

Monitoring these performance indicators is essential for validating the safety and robustness of Brain–Computer Interface systems, particularly in applications involving autonomous robots or assistive technologies.

The generated performance summary provides quantitative evidence supporting the effectiveness of the developed real-time prediction pipeline.

---

## Conclusion

The real-time monitoring module successfully evaluated the operational performance of the Hybrid Adaptive BCI system.

Multiple statistical indicators were computed and stored for future analysis.

These evaluation results verify the stability of the complete online processing pipeline and prepare the system for the final reporting stage and subsequent robotic integration.