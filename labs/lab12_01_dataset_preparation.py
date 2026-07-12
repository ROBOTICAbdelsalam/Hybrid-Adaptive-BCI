import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

print("=" * 60)
print("Lab12.1 - Deep Learning Dataset Preparation")
print("=" * 60)

# --------------------------------------------------
# Create Output Directories
# --------------------------------------------------

os.makedirs("dl_data", exist_ok=True)
os.makedirs("results", exist_ok=True)

# --------------------------------------------------
# Load Machine Learning Dataset
# --------------------------------------------------

X_train = pd.read_csv("ml_data/X_train.csv").values
X_test = pd.read_csv("ml_data/X_test.csv").values

y_train = pd.read_csv("ml_data/y_train.csv").squeeze()
y_test = pd.read_csv("ml_data/y_test.csv").squeeze()

print("Training Samples :", X_train.shape[0])
print("Testing Samples  :", X_test.shape[0])

# --------------------------------------------------
# Encode Labels
# --------------------------------------------------

encoder = LabelEncoder()

y_train = encoder.fit_transform(y_train)
y_test = encoder.transform(y_test)

print("Classes :", encoder.classes_)

# --------------------------------------------------
# Reshape Dataset for Deep Learning
# --------------------------------------------------

X_train = X_train.reshape(
    X_train.shape[0],
    X_train.shape[1],
    1
)

X_test = X_test.reshape(
    X_test.shape[0],
    X_test.shape[1],
    1
)

print("Training Shape :", X_train.shape)
print("Testing Shape  :", X_test.shape)

# --------------------------------------------------
# Save Dataset
# --------------------------------------------------

np.save("dl_data/X_train.npy", X_train)
np.save("dl_data/X_test.npy", X_test)

np.save("dl_data/y_train.npy", y_train)
np.save("dl_data/y_test.npy", y_test)

print("Deep Learning Dataset Saved.")

# --------------------------------------------------
# Save Label Encoder
# --------------------------------------------------

import joblib

joblib.dump(
    encoder,
    "dl_data/label_encoder.pkl"
)

# --------------------------------------------------
# Save Report
# --------------------------------------------------

with open(
    "results/lab12_01_dataset_preparation_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab12.1 - Deep Learning Dataset Preparation\n")
    report.write("=" * 60 + "\n\n")

    report.write(f"Training Samples : {X_train.shape[0]}\n")
    report.write(f"Testing Samples  : {X_test.shape[0]}\n\n")

    report.write(f"Training Shape : {X_train.shape}\n")
    report.write(f"Testing Shape  : {X_test.shape}\n\n")

    report.write("Classes\n")
    report.write("-" * 30 + "\n")

    for c in encoder.classes_:
        report.write(f"{c}\n")

print("Label Encoder Saved.")
print("Report Saved.")

print("\nLab12.1 Finished Successfully.")