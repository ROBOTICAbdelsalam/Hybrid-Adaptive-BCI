# Lab 07.7 – Before vs After Comparison

# 1. Introduction

The final stage of the Independent Component Analysis (ICA) preprocessing workflow is to compare the EEG recording before and after artifact removal.

This comparison provides a visual and qualitative evaluation of the effectiveness of the ICA preprocessing procedure. By examining both recordings, it is possible to observe the reduction of physiological artifacts while preserving the underlying neural activity.

In this laboratory, the original EEG recording was compared with the cleaned EEG recording generated after ICA artifact removal.

---

# 2. Objectives

The objectives of this laboratory were:

- Compare the original EEG recording with the cleaned EEG recording.
- Evaluate the effectiveness of ICA artifact removal.
- Verify that the EEG signal quality was improved.
- Generate a comparison report.
- Prepare the EEG recording for Epoch Creation.

---

# 3. Scientific Background

Independent Component Analysis improves EEG signal quality by separating neural activity from physiological artifacts.

After removing the selected ICA components, the reconstructed EEG recording should contain fewer unwanted artifacts while maintaining the essential brain activity required for further processing.

Visual comparison is an effective method for verifying that the preprocessing stage has been completed successfully.

---

# 4. Methodology

The following procedure was performed:

1. Load the original EEG recording.
2. Load the cleaned EEG recording.
3. Display both recordings.
4. Compare signal quality.
5. Generate the comparison report.

---

# 5. Code Explanation

The implemented Python program loads both the original and cleaned EEG recordings.

The two recordings are displayed for comparison to evaluate the impact of ICA artifact removal.

The comparison confirms that the preprocessing pipeline successfully reduced physiological artifacts before the next stage of EEG analysis.

---

# 6. Generated Outputs

The laboratory generated the following report:

```text
results/lab07_07_before_after_comparison_report.txt
```

If comparison figures were generated, they should also be included in the project documentation.

Example:

```text
figures/lab07_before_after_comparison.png
```

---

# 7. Results

The comparison demonstrated the effect of ICA artifact removal on the EEG recording.

The cleaned EEG signal exhibited reduced physiological artifacts while preserving the neural information required for subsequent processing stages.

The preprocessing pipeline was therefore considered successful.

---

# 8. Discussion

Comparing the EEG recording before and after artifact removal provides an important quality assessment of the preprocessing workflow.

This step confirms that the selected ICA components were removed successfully without introducing significant distortion to the remaining EEG signal.

The cleaned recording is now suitable for Epoch Creation, Feature Extraction, Machine Learning, and Deep Learning.

---

# 9. Conclusion

Lab 07.7 successfully completed the evaluation of the ICA preprocessing workflow.

The comparison between the original and cleaned EEG recordings demonstrated the effectiveness of the artifact removal process.

This laboratory concludes the EEG preprocessing phase of the Hybrid-Adaptive-BCI project and prepares the dataset for the next stage of analysis.

---

# 10. Files Used

## Python Script

```text
labs/lab07_07_before_after_comparison.py
```

## Generated Report

```text
results/lab07_07_before_after_comparison_report.txt
```

## Documentation

```text
docs/Lab07_07_Before_After_Comparison.md
```

---

# 11. References

1. Gramfort A., et al. *MNE Software for Processing MEG and EEG Data.*

2. Hyvärinen A. *Fast Independent Component Analysis.*

3. Makeig S., et al. *Independent Component Analysis of Electroencephalographic Data.*

---

# 12. Next Laboratory
---

# Original EEG

![Original EEG](images/lab07_original_eeg.png)

**Figure 1.** Original EEG recording before artifact removal.

---

# Cleaned EEG

![Cleaned EEG](images/lab07_cleaned_eeg.png)

**Figure 2.** EEG recording after ICA artifact removal.

---

# Figure Analysis

The comparison demonstrates the effect of ICA-based artifact removal.

The cleaned EEG recording contains fewer physiological artifacts while maintaining the neural information required for Brain–Computer Interface analysis.

This confirms the effectiveness of the preprocessing pipeline implemented in the Hybrid-Adaptive-BCI project.

**Lab 08 – Epoch Creation**

The next laboratory introduces EEG epoch generation, where continuous EEG recordings are segmented into shorter time intervals for feature extraction and machine learning applications.