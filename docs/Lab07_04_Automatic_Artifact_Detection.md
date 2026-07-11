# Lab 07.4 – Automatic Artifact Detection

# 1. Introduction

After manually inspecting the Independent Component Analysis (ICA) components, the next step is to automatically identify components that may correspond to physiological artifacts. Automatic artifact detection reduces the amount of manual inspection required and provides an additional verification step before removing unwanted components.

In this laboratory, the automatic artifact detection functions provided by the MNE-Python framework were used to identify ICA components associated with eye-related artifacts.

---

# 2. Objectives

The objectives of this laboratory were:

- Load the trained ICA model.
- Apply automatic artifact detection.
- Identify artifact-related ICA components.
- Record the detected component indices.
- Generate an automatic detection report.

---

# 3. Scientific Background

Physiological artifacts such as eye blinks and eye movements frequently contaminate EEG recordings.

Although manual inspection is reliable, it can be time-consuming and may vary between researchers.

Modern EEG processing frameworks such as MNE-Python provide automatic methods for detecting artifact-related ICA components based on statistical characteristics and signal correlation.

Automatic detection assists the researcher by highlighting components that are likely to represent physiological artifacts.

---

# 4. Automatic Artifact Detection

Automatic artifact detection analyses the ICA components and estimates which components are most likely to correspond to artifacts.

The detected component indices are suggested for review before artifact removal.

Automatic detection is intended to support the manual inspection process rather than replace it completely.

---

# 5. Methodology

The following procedure was performed:

1. Load the filtered EEG recording.
2. Load the trained ICA model.
3. Apply the automatic artifact detection function.
4. Identify candidate artifact components.
5. Generate the detection report.

---

# 6. Code Explanation

The implemented Python program loads the trained ICA model and applies the automatic artifact detection functionality available in the MNE-Python framework.

The detected ICA component indices are displayed and stored for use during the artifact removal stage.

This procedure provides a fast and consistent method for identifying potential physiological artifacts.

---

# 7. Generated Report

The laboratory generated the following report:

```text
results/lab07_04_auto_component_detection_report.txt
```

The report contains the automatically detected ICA component indices.

---

# 8. Results

The automatic detection process completed successfully.

Potential artifact components were identified automatically.

The detected components will be reviewed before removal during the following laboratory.

---

# 9. Discussion

Automatic artifact detection provides an efficient way to identify ICA components that may correspond to physiological artifacts.

Although the algorithm significantly reduces manual effort, the detected components should always be reviewed to ensure that useful neural activity is not removed unintentionally.

Combining automatic detection with manual inspection provides a reliable preprocessing workflow for EEG signal analysis.

---

# 10. Conclusion

Lab 07.4 successfully performed automatic artifact detection using the trained ICA model.

The detected component indices provide valuable information for the artifact removal stage and improve the reliability of the EEG preprocessing pipeline.

---

# 11. Files Used

## Python Script

```text
labs/lab07_04_auto_component_detection.py
```

## Generated Report

```text
results/lab07_04_auto_component_detection_report.txt
```

## Documentation

```text
docs/Lab07_04_Automatic_Artifact_Detection.md
```

---

# 12. References

1. Gramfort A., et al. *MNE Software for Processing MEG and EEG Data.*

2. Hyvärinen A. *Fast Independent Component Analysis.*

3. Makeig S., et al. *Independent Component Analysis of Electroencephalographic Data.*

---

# 13. Next Laboratory

**Lab 07.5 – Manual Artifact Removal**

The next laboratory focuses on removing the manually selected ICA components and reconstructing the cleaned EEG recording.