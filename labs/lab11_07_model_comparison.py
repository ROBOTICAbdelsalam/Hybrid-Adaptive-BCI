import os
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("Lab11.7 - Model Comparison")
print("=" * 60)

os.makedirs("results", exist_ok=True)
os.makedirs("figures", exist_ok=True)
os.makedirs("docs/images", exist_ok=True)

# --------------------------------------------------
# Enter Your Results
# --------------------------------------------------

results = pd.DataFrame({

    "Model": [
        "SVM",
        "Random Forest",
        "XGBoost"
    ],

 "Accuracy": [
    0.8333,
    0.6667,
    0.8333
],

"Precision": [
    0.7083,
    0.6667,
    0.7083
],

"Recall": [
    0.8333,
    0.6667,
    0.8333
],

"F1 Score": [
    0.7619,
    0.6667,
    0.7619
]
})

# --------------------------------------------------
# Save CSV
# --------------------------------------------------

results.to_csv(
    "results/lab11_07_model_comparison.csv",
    index=False
)

# --------------------------------------------------
# Best Model
# --------------------------------------------------

best = results.loc[
    results["Accuracy"].idxmax()
]

# --------------------------------------------------
# Plot
# --------------------------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    results["Model"],
    results["Accuracy"]
)

plt.ylabel("Accuracy")

plt.title("Machine Learning Model Comparison")

plt.ylim(0,1)

plt.savefig(
    "figures/lab11_model_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    "docs/images/lab11_model_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# --------------------------------------------------
# Report
# --------------------------------------------------

with open(
    "results/lab11_07_model_comparison_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab11.7 - Model Comparison\n")
    report.write("="*60 + "\n\n")

    report.write(results.to_string(index=False))

    report.write("\n\n")

    report.write(
        f"Best Model : {best['Model']}\n"
    )

    report.write(
        f"Accuracy   : {best['Accuracy']:.4f}\n"
    )

print(results)

print("\nBest Model :", best["Model"])

print("\nComparison Report Saved.")

print("\nLab11.7 Finished Successfully.")