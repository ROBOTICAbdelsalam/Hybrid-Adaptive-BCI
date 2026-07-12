import os
import pandas as pd

print("=" * 60)
print("Lab11.1 - Dataset Preparation")
print("=" * 60)

os.makedirs("results", exist_ok=True)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

dataset = pd.read_csv("csp/csp_dataset.csv")

print("\nDataset Loaded Successfully.")

samples = dataset.shape[0]
features = dataset.shape[1]

print(f"Samples  : {samples}")
print(f"Features : {features}")

# --------------------------------------------------
# Dataset Information
# --------------------------------------------------

missing = dataset.isnull().sum().sum()

print(f"Missing Values : {missing}")

print("\nData Types:")
print(dataset.dtypes)

# --------------------------------------------------
# Save Report
# --------------------------------------------------

with open(
    "results/lab11_01_dataset_preparation_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab11.1 - Dataset Preparation\n")
    report.write("=" * 55 + "\n\n")

    report.write(f"Samples        : {samples}\n")
    report.write(f"Features       : {features}\n")
    report.write(f"Missing Values : {missing}\n\n")

    report.write("Columns\n")
    report.write("-" * 55 + "\n")

    for column in dataset.columns:
        report.write(column + "\n")

print("\nReport Saved.")

print("\nLab11.1 Finished Successfully.")
