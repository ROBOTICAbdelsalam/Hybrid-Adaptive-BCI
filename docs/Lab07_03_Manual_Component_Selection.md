# Lab 07.3 – Manual Component Selection

# 1. Introduction

Following the visualization of the Independent Component Analysis (ICA) components in the previous laboratory, the next step is to inspect each component manually. The objective of this stage is to identify components that are likely to represent physiological artifacts before applying any modification to the EEG recording.

Manual component selection is an essential preprocessing step because it allows the researcher to distinguish useful neural activity from unwanted signals based on visual inspection.

---

# 2. Objectives

The objectives of this laboratory were:

- Load the trained ICA model.
- Display all independent components.
- Inspect each component manually.
- Record the selected component indices.
- Prepare the EEG recording for artifact removal.

---

# 3. Scientific Background

Each ICA component represents an independent signal source estimated from the EEG recording.

Some components correspond to genuine brain activity, while others represent unwanted artifacts such as eye blinks, eye movements, muscle activity, or electrical interference.

Manual inspection helps determine which components should be considered for removal during the following preprocessing stages.

---

# 4. Manual Component Selection

During this laboratory, every ICA component was visually inspected.

The inspection focused on identifying components that appeared to contain physiological artifacts.

Only the component numbers were recorded during this stage.

No EEG data were modified or reconstructed.

---

# 5. Methodology

The following procedure was performed:

1. Load the EEG dataset.
2. Apply EEG filtering.
3. Train the ICA model.
4. Display the ICA components.
5. Inspect each component manually.
6. Record the selected component indices.
7. Generate the laboratory report.

---

# 6. Code Explanation

The implemented Python program loads the filtered EEG recording and trains the ICA model.

After estimating the independent components, the program displays all components for manual inspection.

The researcher reviews each component and records the indices of components that are considered artifacts.

The selected component indices are stored for use during the artifact removal stage.

---

# 7. Generated Figure

The laboratory generated the following visualization:

```text
figures/lab07_ica_components_page_1.png
```

إذا أضفت الصورة داخل مجلد `docs/images` فاستخدم:

```markdown
![ICA Components](images/lab07_ica_components_page_1.png)
```

**Figure 1.** ICA components generated using the FastICA algorithm.

---

# 8. Figure Analysis

Figure 1 presents the independent components estimated during ICA decomposition.

Each panel represents one independent component extracted from the EEG recording.

The visualization enables manual inspection of all components before any artifact removal is performed.

The selected component indices will be used during the following laboratories.

---

# 9. Generated Report

The following report was generated:

```text
results/lab07_03_manual_component_selection_report.txt
```

The report documents the completion of the manual component selection process.

---

# 10. Results

The ICA components were successfully displayed.

Manual inspection was completed.

The selected component indices were recorded successfully.

The EEG recording remained unchanged during this laboratory.

---

# 11. Discussion

Manual component selection represents an important quality control step before artifact removal.

Careful inspection reduces the possibility of removing components that contain useful neural information.

The selected components will be used in the next laboratories to improve EEG signal quality.

---

# 12. Conclusion

Lab 07.3 successfully completed the manual inspection of the ICA components.

The selected component indices are now available for the artifact removal stage.

This laboratory prepares the EEG recording for the following preprocessing operations.

---

# 13. Files Used

## Python Script

```text
labs/lab07_03_manual_component_selection.py
```

## Generated Figure

```text
figures/lab07_ica_components_page_1.png
```

## Generated Report

```text
results/lab07_03_manual_component_selection_report.txt
```

## Documentation

```text
docs/Lab07_03_Manual_Component_Selection.md
```

---

# 14. References

1. Gramfort A., et al. *MNE Software for Processing MEG and EEG Data.*

2. Hyvärinen A. *Fast Independent Component Analysis.*

3. Makeig S., et al. *Independent Component Analysis of Electroencephalographic Data.*

---
---

# Generated Figure

![Manual ICA Inspection](images/lab07_ica_components_page_1.png)

**Figure 1.** ICA components inspected during manual component selection.

---

# Figure Analysis

The ICA components displayed in Figure 1 were visually inspected to identify possible physiological artifacts.

Only the component indices were recorded during this laboratory.

No components were removed at this stage.

# 15. Next Laboratory

**Lab 07.4 – Automatic Artifact Detection**

The next laboratory focuses on automatically identifying ICA components associated with physiological artifacts before EEG reconstruction.