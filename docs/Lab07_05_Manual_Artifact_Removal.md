# Lab 07.5 – Manual Artifact Removal

# 1. Introduction

Following the manual selection of ICA components in the previous laboratory, the next preprocessing stage consists of removing the selected artifact-related components from the EEG recording.

Manual artifact removal enables the reconstruction of a cleaner EEG signal while preserving useful neural activity. This process improves the quality of the EEG recording before feature extraction and machine learning.

In this laboratory, the manually selected ICA components were excluded from the EEG recording using the trained ICA model.

---

# 2. Objectives

The objectives of this laboratory were:

- Load the trained ICA model.
- Load the selected ICA component indices.
- Remove manually selected artifact components.
- Reconstruct the cleaned EEG recording.
- Generate an artifact removal report.

---

# 3. Scientific Background

Independent Component Analysis separates the EEG recording into statistically independent components.

After identifying artifact-related components, these components can be excluded before reconstructing the EEG signal.

Removing artifact components improves signal quality while preserving useful neural information required for Brain–Computer Interface applications.

Manual artifact removal provides complete control over the preprocessing process because the researcher explicitly selects which components should be removed.

---

# 4. Methodology

The following procedure was performed:

1. Load the filtered EEG recording.
2. Load the trained ICA model.
3. Specify the manually selected component indices.
4. Apply ICA reconstruction.
5. Generate the cleaned EEG recording.
6. Save the artifact removal report.

---

# 5. Code Explanation

The implemented Python program loads the trained ICA model together with the filtered EEG recording.

The selected ICA component indices are assigned to the ICA exclusion list.

The ICA model is then applied to reconstruct the EEG recording without the selected components.

Finally, the program generates a report documenting the artifact removal process.

---

# 6. Generated Report

The laboratory generated the following report:

```text
results/lab07_05_artifact_removal_report.txt
```

---

# 7. Results

The manually selected ICA components were successfully removed.

The EEG recording was reconstructed using the remaining independent components.

The cleaned EEG recording is now ready for further preprocessing and comparison.

---
# Cleaned EEG Signal

```text
figures/lab07_manual_cleaned_eeg.png
```

```markdown
![Cleaned EEG](images/lab07_manual_cleaned_eeg.png)
```

**Figure 1.** EEG signal after manual ICA artifact removal.

The figure illustrates the reconstructed EEG recording after excluding the manually selected ICA components. The cleaned signal will be used for comparison with the original EEG recording in Lab 07.7.
# 8. Discussion

Manual artifact removal provides the researcher with complete control over the preprocessing procedure.

Unlike automatic artifact removal, manual removal allows careful verification of every excluded component before reconstructing the EEG signal.

This approach minimizes the risk of removing useful neural activity.

---

# 9. Conclusion

Lab 07.5 successfully removed the manually selected ICA components from the EEG recording.

The reconstructed EEG signal exhibits reduced physiological artifacts and provides an improved foundation for the remaining stages of the Hybrid-Adaptive-BCI project.

---

# 10. Files Used

## Python Script

```text
labs/lab07_05_manual_artifact_removal.py
```

## Generated Report

```text
results/lab07_05_artifact_removal_report.txt
```

## Documentation

```text
docs/Lab07_05_Manual_Artifact_Removal.md
```

---

# 11. References

1. Gramfort A., et al. *MNE Software for Processing MEG and EEG Data.*

2. Hyvärinen A. *Fast Independent Component Analysis.*

3. Makeig S., et al. *Independent Component Analysis of Electroencephalographic Data.*

---
---

# Generated Figure

![Manual Cleaned EEG](images/lab07_manual_cleaned_eeg.png)

**Figure 1.** EEG recording after manual ICA artifact removal.

---

# Figure Analysis

The EEG recording shown above was reconstructed after removing the manually selected ICA components.

The cleaned signal exhibits reduced artifact contamination while preserving the underlying neural activity.

# 12. Next Laboratory

**Lab 07.6 – Automatic Artifact Removal**

The next laboratory focuses on automatically removing ICA components identified by the automatic artifact detection algorithm.