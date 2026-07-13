import os
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("Lab12.5 - Deep Learning Model Comparison")
print("=" * 60)

# --------------------------------------------------
# Create Folders
# --------------------------------------------------

os.makedirs("results", exist_ok=True)
os.makedirs("figures", exist_ok=True)
os.makedirs("docs/images", exist_ok=True)

# --------------------------------------------------
# Read Reports
# --------------------------------------------------

def read_metrics(report_file):

    metrics = {}

    with open(report_file, "r", encoding="utf-8") as f:

        for line in f:

            if ":" not in line:
                continue

            key, value = line.split(":", 1)

            key = key.strip()

            try:
                value = float(value.strip())
                metrics[key] = value
            except:
                pass

    return metrics

cnn = read_metrics("results/lab12_02_cnn_report.txt")

lstm = read_metrics("results/lab12_03_lstm_report.txt")

cnn_lstm = read_metrics("results/lab12_04_cnn_lstm_report.txt")

# --------------------------------------------------
# Create Comparison Table
# --------------------------------------------------

comparison = pd.DataFrame({

    "Model":[
        "CNN",
        "LSTM",
        "CNN-LSTM"
    ],

    "Accuracy":[
        cnn["Accuracy"],
        lstm["Accuracy"],
        cnn_lstm["Accuracy"]
    ],

    "Precision":[
        cnn["Precision"],
        lstm["Precision"],
        cnn_lstm["Precision"]
    ],

    "Recall":[
        cnn["Recall"],
        lstm["Recall"],
        cnn_lstm["Recall"]
    ],

    "F1 Score":[
        cnn["F1 Score"],
        lstm["F1 Score"],
        cnn_lstm["F1 Score"]
    ]
})

print(comparison)

comparison.to_csv(
    "results/lab12_05_model_comparison.csv",
    index=False
)

# --------------------------------------------------
# Best Model
# --------------------------------------------------

best = comparison.loc[
    comparison["Accuracy"].idxmax()
]

print("\nBest Model :", best["Model"])

# --------------------------------------------------
# Accuracy Figure
# --------------------------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    comparison["Model"],
    comparison["Accuracy"]
)

plt.title("Deep Learning Model Accuracy")

plt.ylabel("Accuracy")

plt.savefig(
    "figures/lab12_model_accuracy.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    "docs/images/lab12_model_accuracy.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# --------------------------------------------------
# F1 Figure
# --------------------------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    comparison["Model"],
    comparison["F1 Score"]
)

plt.title("Deep Learning Model F1 Score")

plt.ylabel("F1 Score")

plt.savefig(
    "figures/lab12_model_f1.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    "docs/images/lab12_model_f1.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# --------------------------------------------------
# Report
# --------------------------------------------------

with open(
    "results/lab12_05_model_comparison_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab12.5 - Deep Learning Model Comparison\n")
    report.write("="*60 + "\n\n")

    report.write(comparison.to_string(index=False))

    report.write("\n\n")

    report.write(f"Best Model : {best['Model']}\n")

print("\nComparison Report Saved.")

print("\nLab12.5 Finished Successfully.")