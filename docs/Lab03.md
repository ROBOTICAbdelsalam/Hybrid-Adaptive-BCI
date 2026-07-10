# Lab 03 – EDF File Reading

## Overview

Lab 03 focused on reading Electroencephalography (EEG) recordings stored in the European Data Format (EDF). The EDF format is one of the most widely used standards for storing physiological signals and is fully supported by the MNE-Python framework.

This laboratory verified that EEG recordings could be successfully loaded into memory and prepared for visualization and preprocessing.

---

# Objectives

The objectives of this laboratory were:

- Read EEG recordings from EDF files.
- Load the recordings into memory.
- Verify the integrity of the recording.
- Prepare the data for visualization.
- Understand the structure of raw EEG data.

---

# Background

The European Data Format (EDF) is a standard file format designed for storing physiological signals such as EEG, ECG, EMG, and EOG. It supports multiple synchronized channels and preserves recording metadata, making it suitable for neuroscience and biomedical research.

Within the MNE-Python framework, EDF files are loaded as Raw objects, providing access to signal data, channel information, sampling frequency, recording duration, and metadata.

Reading EEG recordings correctly is an essential step before any preprocessing or machine learning tasks can be performed.

---

# Software and Libraries

The following tools were used:

- Python
- MNE-Python

---

# Methodology

The following steps were performed:

1. Locate the downloaded EDF recording.
2. Load the recording using MNE.
3. Store the recording as a Raw object.
4. Verify successful loading.
5. Prepare the recording for visualization.

---

# Code Explanation

The implemented code performs the following operations:

- Opens the EDF recording.
- Loads all EEG channels into memory.
- Creates an MNE Raw object.
- Makes the data available for subsequent preprocessing operations.

The Raw object serves as the primary data structure throughout the remainder of the project.

---

# Results

The laboratory successfully:

- Loaded the EDF recording.
- Created the Raw EEG object.
- Verified that the recording was readable.
- Prepared the recording for visualization.

---

# Generated Files

Outputs generated during this laboratory include:

- Raw EEG object
- Loaded EDF recording

---

# Discussion

Reading EEG recordings correctly is a critical prerequisite for all subsequent processing stages. Once loaded into memory, the EEG data can be filtered, visualized, segmented, cleaned using ICA, and prepared for machine learning.

The successful completion of this laboratory confirmed that the selected EEG dataset is compatible with the Hybrid-Adaptive-BCI processing pipeline.

---

# Conclusion

Lab 03 successfully demonstrated how EEG recordings stored in EDF format can be loaded and prepared for analysis using MNE-Python. This laboratory provides the foundation for EEG visualization and preprocessing performed in the following laboratories.

---

# Next Laboratory

**Lab 04 – Raw EEG Visualization**

The next laboratory focuses on visualizing the loaded EEG recordings to inspect signal quality before preprocessing.