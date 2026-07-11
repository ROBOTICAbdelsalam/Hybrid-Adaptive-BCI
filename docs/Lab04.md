# Lab 04 – Raw EEG Visualization

## Overview

Lab 04 focused on visualizing the raw Electroencephalography (EEG) signals before applying any preprocessing techniques. Visual inspection of raw EEG recordings is an essential step in Brain–Computer Interface (BCI) research because it allows researchers to evaluate signal quality, identify potential artifacts, and verify that the recording has been loaded correctly.

The MNE-Python visualization tools were used to inspect the EEG recordings interactively.

---

# Objectives

The objectives of this laboratory were:

- Visualize raw EEG signals.
- Inspect EEG channel activity.
- Verify signal quality.
- Identify visible artifacts.
- Prepare the recordings for preprocessing.

---

# Background

EEG signals are extremely sensitive to both neural activity and external interference. Before applying filtering or artifact removal techniques, researchers typically inspect the raw recordings to identify potential problems such as eye blinks, muscle activity, electrical noise, or disconnected electrodes.

Visual inspection provides valuable information about signal quality and helps determine whether additional preprocessing steps are required.

---

# Software and Libraries

The following software was used:

- Python
- MNE-Python
- Matplotlib

---

# Methodology

The visualization process consisted of the following steps:

1. Load the raw EEG recording.
2. Open the interactive MNE visualization window.
3. Display all EEG channels.
4. Inspect the waveform of each channel.
5. Observe recording quality and identify visible artifacts.

The visualization was performed before any filtering or artifact removal.

---

# Code Explanation

The implemented code displays the EEG recording using the MNE interactive viewer.

The visualization enables:

- Channel scrolling
- Zooming
- Time navigation
- Signal amplitude inspection

These interactive tools assist in understanding the characteristics of the recorded EEG signals.

---

# Results

The laboratory successfully displayed the raw EEG recordings.

The visualization confirmed:

- Successful dataset loading.
- Proper channel configuration.
- Continuous EEG recording.
- Presence of naturally occurring EEG activity.

The generated figure was saved for documentation purposes.

---

# Generated Files

Outputs generated during this laboratory include:

- Raw EEG visualization
- EEG figure stored in the `figures` directory

---

# Discussion

Visualizing raw EEG recordings is a fundamental step in EEG analysis. It allows researchers to detect obvious recording problems before applying preprocessing algorithms.

This laboratory also provides an important baseline for comparing EEG signals before and after filtering and artifact removal.

---

# Conclusion

Lab 04 successfully demonstrated how raw EEG recordings can be visualized using the MNE-Python framework. The generated visualization confirmed that the EEG recordings were correctly loaded and ready for preprocessing in subsequent laboratories.

---

# Next Laboratory

**Lab 05 – Dataset Inspection**

The next laboratory focuses on examining the recording metadata, including channel information, sampling frequency, recording duration, and dataset characteristics.