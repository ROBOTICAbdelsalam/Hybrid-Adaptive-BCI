import os
import pandas as pd

print("=" * 60)
print("Lab10.6 - Final CSP Report")
print("=" * 60)

os.makedirs("results", exist_ok=True)

# --------------------------------------------------
# Load Final CSP Dataset
# --------------------------------------------------

df = pd.read_csv("csp/csp_dataset.csv")

samples = df.shape[0]
features = df.shape[1]
missing = int(df.isnull().sum().sum())

# --------------------------------------------------
# Final Report
# --------------------------------------------------

with open(
    "results/lab10_06_csp_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Chapter 10 - Common Spatial Patterns (CSP)\n")
    report.write("=" * 60 + "\n\n")

    report.write("Completed Laboratories\n")
    report.write("----------------------\n")
    report.write("Lab10.1 - CSP Theory\n")
    report.write("Lab10.2 - Train CSP\n")
    report.write("Lab10.3 - Transform EEG Signals\n")
    report.write("Lab10.4 - CSP Feature Analysis\n")
    report.write("Lab10.5 - Save CSP Features\n\n")

    report.write("Final Dataset Summary\n")
    report.write("----------------------\n")
    report.write(f"Samples           : {samples}\n")
    report.write(f"Features          : {features}\n")
    report.write(f"Missing Values    : {missing}\n\n")

    report.write("Generated Files\n")
    report.write("----------------------\n")
    report.write("csp/csp_model.pkl\n")
    report.write("csp/csp_features.csv\n")
    report.write("csp/csp_dataset.csv\n\n")

    report.write("Results\n")
    report.write("----------------------\n")
    report.write("The CSP feature extraction pipeline completed successfully.\n")
    report.write("The generated dataset is ready for Machine Learning classification.\n")

print("Final Report Saved.")

print("\nLab10.6 Finished Successfully.")
