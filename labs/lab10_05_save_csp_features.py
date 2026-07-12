import os
import shutil
import pandas as pd

print("=" * 60)
print("Lab10.5 - Save CSP Features")
print("=" * 60)

os.makedirs("csp", exist_ok=True)
os.makedirs("results", exist_ok=True)
os.makedirs("docs/images", exist_ok=True)

# --------------------------------------------------
# Load CSP Features
# --------------------------------------------------

df = pd.read_csv("csp/csp_features.csv")

print(f"Samples  : {df.shape[0]}")
print(f"Features : {df.shape[1]}")

# --------------------------------------------------
# Check Missing Values
# --------------------------------------------------

missing = df.isnull().sum().sum()

print(f"Missing Values : {missing}")

# --------------------------------------------------
# Save Final Dataset
# --------------------------------------------------

output_file = "csp/csp_dataset.csv"

df.to_csv(
    output_file,
    index=False
)

print("Final CSP Dataset Saved.")

# --------------------------------------------------
# Generate Summary
# --------------------------------------------------

summary = pd.DataFrame({
    "Metric": [
        "Samples",
        "Features",
        "Missing Values"
    ],
    "Value": [
        df.shape[0],
        df.shape[1],
        missing
    ]
})

summary.to_csv(
    "results/lab10_05_csp_dataset_summary.csv",
    index=False
)

# --------------------------------------------------
# Report
# --------------------------------------------------

with open(
    "results/lab10_05_save_csp_features_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab10.5 - Save CSP Features\n")
    report.write("=" * 50 + "\n\n")

    report.write(f"Samples        : {df.shape[0]}\n")
    report.write(f"Features       : {df.shape[1]}\n")
    report.write(f"Missing Values : {missing}\n")
    report.write("\nDataset successfully prepared for Machine Learning.\n")

print("Report Saved.")

print("\nLab10.5 Finished Successfully.")
