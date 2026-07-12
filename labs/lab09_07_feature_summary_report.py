import pandas as pd
import os

print("=" * 60)
print("Lab09.7 - Feature Summary Report")
print("=" * 60)

# Load Final Feature Matrix
features = pd.read_csv("features/final_feature_matrix.csv")

os.makedirs("results", exist_ok=True)

# Generate Report
with open(
    "results/lab09_07_feature_summary_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab09.7 - Feature Summary Report\n")
    report.write("=" * 55 + "\n\n")

    report.write(f"Number of Epochs      : {features.shape[0]}\n")
    report.write(f"Selected Features     : {features.shape[1]}\n\n")

    report.write("Feature Names\n")
    report.write("-" * 55 + "\n")

    for col in features.columns:
        report.write(col + "\n")

print("\nSummary Report Saved.")
print("\nLab09.7 Finished Successfully.")
