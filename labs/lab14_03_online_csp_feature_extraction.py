import os
import numpy as np
import pandas as pd

print("=" * 60)
print("Lab14.3 - Online CSP Feature Extraction")
print("=" * 60)

# --------------------------------------------------
# Create Output Folder
# --------------------------------------------------

os.makedirs("realtime/results", exist_ok=True)

# --------------------------------------------------
# Load Preprocessed EEG
# --------------------------------------------------

input_file = "realtime/data/preprocessed_eeg.csv"

if not os.path.exists(input_file):
    print("Preprocessed EEG file not found.")
    exit()

eeg = pd.read_csv(input_file)

print("\nPreprocessed EEG Shape")
print(eeg.shape)

# --------------------------------------------------
# Window Configuration
# --------------------------------------------------

window_size = 250          # 1 second @250Hz
num_windows = len(eeg) // window_size

print(f"\nWindow Size : {window_size}")
print(f"Number of Windows : {num_windows}")

# --------------------------------------------------
# Feature Extraction
# --------------------------------------------------

features = []

for i in range(num_windows):

    start = i * window_size
    end = start + window_size

    window = eeg.iloc[start:end]

    # Variance of each EEG channel
    variance = np.var(window.values, axis=0)

    # Log-Variance
    log_variance = np.log(variance + 1e-10)

    # --------------------------------------------------
    # IMPORTANT
    # CNN expects ONLY 4 input features
    # --------------------------------------------------

    feature_vector = log_variance[:4]

    features.append(feature_vector)

# --------------------------------------------------
# Convert to DataFrame
# --------------------------------------------------

features = np.array(features)

feature_names = [
    "Feature_1",
    "Feature_2",
    "Feature_3",
    "Feature_4"
]

features_df = pd.DataFrame(
    features,
    columns=feature_names
)

# --------------------------------------------------
# Save Features
# --------------------------------------------------

output_file = "realtime/data/realtime_features.csv"

features_df.to_csv(
    output_file,
    index=False
)

print("\nFeatures Saved Successfully.")

print("\nFeature Matrix Shape")
print(features_df.shape)

print("\nExtracted Features")
print(features_df)

# --------------------------------------------------
# Statistics
# --------------------------------------------------

print("\nFeature Statistics")
print(features_df.describe())

# --------------------------------------------------
# Save Report
# --------------------------------------------------

report_file = "realtime/results/lab14_03_feature_extraction_report.txt"

with open(report_file, "w", encoding="utf-8") as report:

    report.write("Lab14.3 - Online CSP Feature Extraction\n")
    report.write("=" * 60 + "\n\n")

    report.write(f"Input File      : {input_file}\n")
    report.write(f"Output File     : {output_file}\n")
    report.write(f"Window Size     : {window_size}\n")
    report.write(f"Number Windows  : {num_windows}\n")
    report.write(f"Output Features : {features_df.shape[1]}\n")
    report.write(f"Feature Matrix  : {features_df.shape}\n")

print("\nReport Saved.")

print("\nLab14.3 Finished Successfully.")