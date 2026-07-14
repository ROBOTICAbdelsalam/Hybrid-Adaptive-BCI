# Lab 14.3 – Online CSP Feature Extraction

## Objective

The objective of this laboratory is to extract discriminative EEG features from the preprocessed real-time signals using an online Common Spatial Pattern (CSP)-inspired feature extraction strategy.

The extracted features provide a compact representation of the EEG activity and serve as the direct input for the real-time classification stage developed in the following laboratory.

---

## Background

Feature extraction is one of the most important stages in Brain–Computer Interface (BCI) systems.

Instead of directly classifying raw EEG signals, informative features are extracted to improve classification accuracy while reducing computational complexity.

Common Spatial Pattern (CSP) is one of the most widely used feature extraction methods for Motor Imagery BCI because it maximizes the variance differences between different brain activity classes.

During real-time operation, EEG data are divided into consecutive windows, and statistical features are extracted from each window for immediate classification.

---

## Python Script

```
labs/lab14_03_online_csp_feature_extraction.py
```

---

## Input File

### Preprocessed EEG Signal

```
realtime/data/preprocessed_eeg.csv
```

---

## Processing Steps

1. Load the preprocessed EEG dataset.
2. Divide the continuous EEG signal into fixed-size windows.
3. Compute the variance of each EEG channel.
4. Apply logarithmic variance transformation.
5. Generate CSP-inspired feature vectors.
6. Store the extracted feature matrix.
7. Generate the feature extraction report.

---

## Feature Extraction Parameters

| Parameter | Value |
|-----------|------:|
| Window Size | 250 Samples |
| Sampling Rate | 250 Hz |
| Window Duration | 1 Second |
| Feature Type | Log-Variance (CSP-Inspired) |

---

## Generated Files

### Extracted Feature Matrix

```
realtime/data/realtime_features.csv
```

### Feature Extraction Report

```
realtime/results/lab14_03_feature_extraction_report.txt
```

---

## Experimental Result

The real-time feature extraction stage successfully generated one feature vector for each EEG window.

Each feature vector contains the logarithmic variance of all EEG channels and represents the EEG activity during one second of recording.

---

## Example Console Output

```
============================================================
Lab14.3 - Online CSP Feature Extraction
============================================================

Preprocessed EEG Shape

(1250, 8)

Window Size : 250

Number of Windows : 5

Features Saved Successfully.

Feature Matrix Shape

(5, 8)

Report Saved.

Lab14.3 Finished Successfully.
```

---

## Generated Feature Matrix

Example structure:

| CSP_Feature_1 | CSP_Feature_2 | CSP_Feature_3 | CSP_Feature_4 | CSP_Feature_5 | CSP_Feature_6 | CSP_Feature_7 | CSP_Feature_8 |
|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|--------------:|
| ... | ... | ... | ... | ... | ... | ... | ... |

---

## Discussion

The feature extraction stage converts continuous EEG signals into compact numerical representations that are suitable for machine learning and deep learning models.

Instead of processing thousands of EEG samples directly, the classifier receives a small set of informative features extracted from each time window.

Although a simplified CSP-inspired approach based on logarithmic variance is implemented in this laboratory, the software architecture is fully compatible with a trained CSP transformation matrix that can be incorporated in future versions of the system.

This design enables a smooth transition from simulated real-time processing to a fully operational Brain–Computer Interface using real EEG hardware.

---

## Conclusion

The online feature extraction stage was successfully implemented.

The preprocessed EEG stream was segmented into one-second windows, and CSP-inspired logarithmic variance features were extracted for every EEG channel.

The generated feature matrix represents the input for the next laboratory, where real-time classification will be performed using the trained artificial intelligence models developed in the previous chapters.