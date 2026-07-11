# Lab 05 – EEG Dataset Inspection

# 1. Introduction

The successful development of any Brain–Computer Interface (BCI) system begins with a comprehensive understanding of the acquired Electroencephalography (EEG) data. Before applying preprocessing techniques such as filtering or Independent Component Analysis (ICA), it is essential to inspect the dataset to ensure that all recording parameters are valid and suitable for subsequent signal processing.

EEG dataset inspection is considered one of the most important quality assurance procedures in biomedical signal processing. Incorrect assumptions regarding sampling frequency, channel configuration, recording duration, or electrode information may significantly affect preprocessing quality and ultimately reduce the performance of machine learning models.

In this laboratory, the EEGBCI dataset was inspected using the MNE-Python framework to verify the integrity of the recording and extract the metadata required for the following stages of the Hybrid-Adaptive-BCI project.

---

# 2. Objectives

The primary objectives of this laboratory were:

- Verify that the EEG recording was loaded correctly.
- Inspect the recording metadata.
- Determine the number of EEG channels.
- Verify the sampling frequency.
- Inspect recording duration.
- Examine channel names.
- Validate recording integrity.
- Generate an inspection report for future reference.

---

# 3. Scientific Background

An EEG recording contains two categories of information.

The first category consists of the recorded electrical brain activity.

The second category consists of metadata describing how the recording was acquired.

Examples include:

- Number of channels
- Channel names
- Sampling frequency
- Recording duration
- Electrode montage
- Measurement information
- Coordinate system

Although these parameters are not part of the EEG waveform itself, they are essential for every preprocessing operation performed later.

For example, digital filters require an accurate sampling frequency, while ICA depends on correct channel information to separate independent components successfully.

Therefore, dataset inspection is considered the first validation stage before any signal processing begins.

---

# 4. Dataset Description

The Hybrid-Adaptive-BCI project utilizes the EEGBCI dataset available through the MNE-Python framework.

Dataset characteristics include:

- Public benchmark dataset
- EDF recording format
- Multiple subjects
- Motor imagery experiments
- Standard EEG electrode placement
- High-quality research recordings

The dataset is widely used within the Brain–Computer Interface research community and provides an excellent benchmark for evaluating EEG preprocessing algorithms.

---

# 5. Software Environment

The laboratory was implemented using the following software:

- Python
- MNE-Python
- NumPy
- Visual Studio Code

The MNE framework provides direct access to recording metadata through the Raw object.

---

# 6. Methodology

The inspection procedure consisted of several sequential steps.

## Step 1

Load the EEG recording into memory.

---

## Step 2

Create the Raw object.

---

## Step 3

Read recording metadata.

---

## Step 4

Extract recording information.

---

## Step 5

Display channel information.

---

## Step 6

Verify sampling frequency.

---

## Step 7

Determine recording duration.

---

## Step 8

Generate the inspection report.

---

# 7. Code Explanation

The implemented Python program automatically extracts metadata stored inside the Raw object.

The extracted information includes:

- Number of EEG channels
- Sampling frequency
- Recording duration
- Channel names
- Recording information

Finally, the program stores all extracted information inside a text report located in the project results directory.

This automated reporting procedure improves reproducibility and allows future verification of the dataset characteristics.

---

# 8. Results

The inspection process confirmed that:

- The recording was successfully loaded.
- Metadata was correctly extracted.
- EEG channels were correctly recognized.
- Recording duration was successfully determined.
- Sampling frequency was correctly identified.
- The recording was suitable for preprocessing.

---

# 9. Generated Output

The laboratory generated the following output:

```
results/lab05_dataset_info.txt
```

The report contains all relevant recording metadata and serves as permanent documentation of the dataset characteristics.

---

# 10. Discussion

Dataset inspection is frequently overlooked by beginners; however, experienced EEG researchers consider it an essential preprocessing step.

Incorrect metadata may produce serious problems during:

- Digital filtering
- ICA decomposition
- Epoch generation
- Feature extraction
- Machine Learning

By validating the recording before preprocessing, these potential issues can be identified early.

Furthermore, automatic report generation enhances the reproducibility of the Hybrid-Adaptive-BCI project by documenting exactly which dataset characteristics were used during the experiments.

---

# 11. Conclusion

Lab 05 successfully verified the structural properties of the EEG recording.

The generated inspection report confirmed that the recording satisfies all requirements for subsequent preprocessing stages.

This laboratory therefore establishes the quality assurance foundation for the remaining stages of the Hybrid-Adaptive-BCI processing pipeline.

---

# 12. Key Outcomes

After completing this laboratory, the project achieved the following:

- Successful metadata extraction.
- Verification of EEG recording integrity.
- Automatic report generation.
- Preparation for digital filtering.
- Improved experimental reproducibility.

---

# 13. References

1. Gramfort A., et al. *MNE Software for Processing MEG and EEG Data*. NeuroImage.

2. Goldberger AL., et al. *PhysioBank, PhysioToolkit, and PhysioNet*.

3. Niedermeyer E., Silva FL. *Electroencephalography: Basic Principles, Clinical Applications and Related Fields.*

---

# 14. Next Laboratory

**Lab 06 – EEG Signal Filtering**

The next laboratory focuses on improving EEG signal quality through digital band-pass filtering before artifact removal using Independent Component Analysis.