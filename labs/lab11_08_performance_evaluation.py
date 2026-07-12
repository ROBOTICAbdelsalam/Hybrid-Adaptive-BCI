import os
import pandas as pd

print("=" * 60)
print("Lab11.8 - Performance Evaluation")
print("=" * 60)

os.makedirs("results", exist_ok=True)

# --------------------------------------------------
# Load Comparison Results
# --------------------------------------------------

results = pd.read_csv(
    "results/lab11_07_model_comparison.csv"
)

print(results)

# --------------------------------------------------
# Best Model
# --------------------------------------------------

best_model = results.loc[
    results["Accuracy"].idxmax()
]

# --------------------------------------------------
# Average Performance
# --------------------------------------------------

avg_accuracy = results["Accuracy"].mean()
avg_precision = results["Precision"].mean()
avg_recall = results["Recall"].mean()
avg_f1 = results["F1 Score"].mean()

# --------------------------------------------------
# Save Report
# --------------------------------------------------

with open(
    "results/lab11_08_performance_evaluation_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab11.8 - Performance Evaluation\n")
    report.write("=" * 60 + "\n\n")

    report.write("Machine Learning Models\n")
    report.write("-" * 60 + "\n")
    report.write(results.to_string(index=False))
    report.write("\n\n")

    report.write("Average Performance\n")
    report.write("-" * 60 + "\n")

    report.write(f"Accuracy : {avg_accuracy:.4f}\n")
    report.write(f"Precision: {avg_precision:.4f}\n")
    report.write(f"Recall   : {avg_recall:.4f}\n")
    report.write(f"F1 Score : {avg_f1:.4f}\n\n")

    report.write("Best Performing Model\n")
    report.write("-" * 60 + "\n")

    report.write(f"Model     : {best_model['Model']}\n")
    report.write(f"Accuracy  : {best_model['Accuracy']:.4f}\n")
    report.write(f"Precision : {best_model['Precision']:.4f}\n")
    report.write(f"Recall    : {best_model['Recall']:.4f}\n")
    report.write(f"F1 Score  : {best_model['F1 Score']:.4f}\n")

print("\nAverage Accuracy :", round(avg_accuracy,4))
print("Average Precision:", round(avg_precision,4))
print("Average Recall   :", round(avg_recall,4))
print("Average F1 Score :", round(avg_f1,4))

print("\nBest Model :", best_model["Model"])

print("\nPerformance Report Saved.")

print("\nLab11.8 Finished Successfully.")