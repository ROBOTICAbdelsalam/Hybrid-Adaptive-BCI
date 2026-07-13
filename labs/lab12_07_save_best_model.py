import os
import shutil
import pandas as pd

print("=" * 60)
print("Lab12.7 - Save Best Deep Learning Model")
print("=" * 60)

# --------------------------------------------------
# Create Folder
# --------------------------------------------------

os.makedirs("models", exist_ok=True)
os.makedirs("results", exist_ok=True)

# --------------------------------------------------
# Load Comparison Table
# --------------------------------------------------

comparison = pd.read_csv(
    "results/lab12_05_model_comparison.csv"
)

# --------------------------------------------------
# Select Best Model
# --------------------------------------------------

best = comparison.loc[
    comparison["Accuracy"].idxmax()
]

best_model = best["Model"]

print("\nBest Model :", best_model)

# --------------------------------------------------
# Source Model
# --------------------------------------------------

model_files = {

    "CNN":
    "deep_learning/cnn_classifier.keras",

    "LSTM":
    "deep_learning/lstm_classifier.keras",

    "CNN-LSTM":
    "deep_learning/cnn_lstm_classifier.keras"

}

source = model_files[best_model]

destination = "models/final_deep_learning_model.keras"

# --------------------------------------------------
# Copy Best Model
# --------------------------------------------------

shutil.copy2(source, destination)

print("Best Model Copied Successfully.")

# --------------------------------------------------
# Save Final Report
# --------------------------------------------------

with open(
    "results/lab12_07_final_model_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab12.7 - Save Best Deep Learning Model\n")
    report.write("=" * 60 + "\n\n")

    report.write(f"Selected Model : {best_model}\n")
    report.write(f"Accuracy       : {best['Accuracy']:.4f}\n")
    report.write(f"Precision      : {best['Precision']:.4f}\n")
    report.write(f"Recall         : {best['Recall']:.4f}\n")
    report.write(f"F1 Score       : {best['F1 Score']:.4f}\n\n")

    report.write("Final Model Path\n")
    report.write("--------------------------\n")
    report.write(destination)

print("Final Report Saved.")

print("\n============================================================")
print("Deep Learning Final Model")
print("============================================================")

print(f"Model     : {best_model}")
print(f"Accuracy  : {best['Accuracy']:.4f}")
print(f"Precision : {best['Precision']:.4f}")
print(f"Recall    : {best['Recall']:.4f}")
print(f"F1 Score  : {best['F1 Score']:.4f}")

print("\nModel Saved To:")
print(destination)

print("\nLab12.7 Finished Successfully.")