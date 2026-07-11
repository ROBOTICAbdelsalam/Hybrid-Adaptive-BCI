# Lab 06 – EEG Signal Filtering

# 1. Introduction

Electroencephalography (EEG) recordings are highly susceptible to various sources of interference originating from both physiological and environmental factors. Raw EEG signals often contain low-frequency baseline drift, muscle activity, eye movement artifacts, and high-frequency electrical noise that can significantly reduce signal quality.

Before applying advanced preprocessing techniques such as Independent Component Analysis (ICA), feature extraction, or machine learning algorithms, the EEG signal must first undergo digital filtering. Proper filtering improves the signal-to-noise ratio while preserving the neural information required for Brain–Computer Interface (BCI) applications.

In this laboratory, a digital band-pass filter was applied to the EEGBCI dataset using the MNE-Python framework to retain frequencies between **1 Hz and 40 Hz**, which represent the frequency range most relevant for motor imagery analysis.

---

# 2. Objectives

The objectives of this laboratory were:

- Improve EEG signal quality.
- Remove low-frequency baseline drift.
- Suppress high-frequency electrical noise.
- Preserve useful neural activity.
- Prepare EEG recordings for Independent Component Analysis (ICA).
- Generate filtering documentation.

---

# 3. Scientific Background

EEG signals contain useful brain activity distributed across several frequency bands.

The most commonly analyzed EEG frequency bands include:

| Frequency Band | Range | Typical Function |
|----------------|-------|------------------|
| Delta | 0.5–4 Hz | Deep sleep |
| Theta | 4–8 Hz | Memory and attention |
| Alpha | 8–13 Hz | Relaxation |
| Beta | 13–30 Hz | Motor activity |
| Gamma | >30 Hz | Cognitive processing |

Motor imagery experiments primarily rely on the Alpha and Beta frequency bands.

Consequently, frequencies outside the range of interest may be attenuated using digital filters.

---

# 4. Why Filtering is Necessary

Raw EEG recordings frequently contain unwanted components such as:

- Baseline drift
- Electrode movement
- Power-line interference
- High-frequency electronic noise
- Motion artifacts

If these unwanted components are not removed before further analysis, they may significantly reduce the performance of ICA decomposition and machine learning algorithms.

Filtering therefore represents one of the most important preprocessing stages within any EEG processing pipeline.

---

# 5. Digital Band-Pass Filter

A band-pass filter allows only frequencies located within a specified frequency range to pass while suppressing frequencies outside this interval.

In this laboratory the following parameters were used:

Lower cutoff frequency:

**1 Hz**

Upper cutoff frequency:

**40 Hz**

This frequency range preserves the majority of neural activity relevant for motor imagery while reducing unwanted noise.

---

# 6. Software Environment

The laboratory was implemented using:

- Python
- MNE-Python
- NumPy
- SciPy
- Matplotlib

The MNE-Python framework provides optimized finite impulse response (FIR) filters specifically designed for EEG signal processing.

---

# 7. Methodology

The filtering procedure consisted of the following stages.

## Step 1

Load the EEG recording.

---

## Step 2

Verify recording integrity.

---

## Step 3

Apply a 1–40 Hz band-pass filter.

---

## Step 4

Generate the filtered EEG recording.

---

## Step 5

Save the filtering report.

---

## Step 6

Generate visualization figures.

---

# 8. Code Explanation

The implemented Python program applies an FIR band-pass filter provided by the MNE framework.

The filtering operation removes frequencies below 1 Hz and above 40 Hz while preserving the spectral content required for motor imagery analysis.

The resulting filtered signal becomes the input for Independent Component Analysis (ICA), ensuring improved decomposition quality.

---

# 9. Results

The filtering stage successfully:

- Reduced low-frequency drift.
- Reduced high-frequency noise.
- Improved EEG signal quality.
- Prepared the recording for ICA.

The generated report confirms successful completion of the filtering process.

---

# 10. Generated Outputs

The following outputs were generated during this laboratory:

```
results/lab06_filter_report.txt
```

```
figures/lab06_filtered_eeg.png
```

These outputs document the preprocessing stage and provide visual confirmation of the filtering process.

---

# 11. Discussion

Digital filtering represents one of the most critical preprocessing operations in EEG analysis.

Choosing inappropriate cutoff frequencies may remove important neural information or preserve unwanted noise.

The selected frequency range (1–40 Hz) provides a practical compromise between noise reduction and information preservation for motor imagery applications.

Furthermore, applying filtering before ICA generally improves component separation by reducing broadband interference.

---

# 12. Importance for the Hybrid-Adaptive-BCI Project

The filtered EEG recording generated in this laboratory serves as the primary input for all subsequent processing stages, including:

- Independent Component Analysis (ICA)
- Epoch Generation
- Feature Extraction
- Machine Learning
- Deep Learning
- Adaptive Artificial Intelligence
- ROS2 Robot Control

Therefore, the quality of this filtering stage directly influences the overall performance of the Hybrid-Adaptive-BCI system.

---

# 13. Conclusion

Lab 06 successfully improved EEG signal quality through digital band-pass filtering.

The preprocessing operation removed unwanted frequency components while preserving the neural activity required for Brain–Computer Interface analysis.

The resulting filtered EEG recording is now suitable for Independent Component Analysis (ICA), which represents the next major preprocessing stage within the Hybrid-Adaptive-BCI project.

---

# 14. Key Outcomes

After completing this laboratory, the project achieved:

- Successful digital filtering.
- Improved signal-to-noise ratio.
- Preparation for ICA decomposition.
- Automatic report generation.
- Improved preprocessing reliability.

---

# 15. References

1. Gramfort A., et al. *MNE Software for Processing MEG and EEG Data*. NeuroImage.

2. Luck, S. J. *An Introduction to the Event-Related Potential Technique.*

3. Niedermeyer E., Silva FL. *Electroencephalography: Basic Principles, Clinical Applications and Related Fields.*

---

# 16. Next Laboratory

**Lab 07 – Independent Component Analysis (ICA)**

The next laboratory focuses on separating EEG signals into statistically independent components in order to identify and remove physiological artifacts before feature extraction and machine learning.