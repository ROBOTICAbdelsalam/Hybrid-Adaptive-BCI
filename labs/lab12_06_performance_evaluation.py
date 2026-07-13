import os
import pandas as pd

print("=" * 60)
print("Lab12.6 - Performance Evaluation")
print("=" * 60)

os.makedirs("results", exist_ok=True)

# --------------------------------------------------
# Load Comparison Table
# --------------------------------------------------

comparison = pd.read_csv(
    "results/lab12_05_model_comparison.csv"
)

print(comparison)

# --------------------------------------------------
# Best Model
# --------------------------------------------------

best = comparison.loc[
    comparison["Accuracy"].idxmax()
]

print("\nBest Deep Learning Model")
print("-" * 35)

print(best)

# --------------------------------------------------
# Save Final Evaluation
# --------------------------------------------------

with open(
    "results/lab12_06_performance_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab12.6 - Performance Evaluation\n")
    report.write("=" * 60 + "\n\n")

    report.write("Best Deep Learning Model\n\n")

    report.write(best.to_string())

print("\nPerformance Report Saved.")

print("\nLab12.6 Finished Successfully.")