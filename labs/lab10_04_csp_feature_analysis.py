import os
import shutil
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("Lab10.4 - CSP Feature Analysis")
print("=" * 60)

os.makedirs("figures", exist_ok=True)
os.makedirs("results", exist_ok=True)
os.makedirs("docs/images", exist_ok=True)

# --------------------------------------------------
# Load CSP Features
# --------------------------------------------------

df = pd.read_csv("csp/csp_features.csv")

print(df.describe())

# --------------------------------------------------
# Save Statistics
# --------------------------------------------------

stats = df.describe()

stats.to_csv(
    "results/lab10_04_csp_statistics.csv"
)

print("Statistics Saved.")

# --------------------------------------------------
# Correlation Matrix
# --------------------------------------------------

corr = df.corr()

plt.figure(figsize=(8,6))

plt.imshow(corr, aspect="auto")

plt.colorbar()

plt.xticks(range(len(df.columns)), df.columns, rotation=45)
plt.yticks(range(len(df.columns)), df.columns)

plt.title("CSP Feature Correlation Matrix")

plt.tight_layout()

plt.savefig(
    "figures/lab10_csp_correlation.png",
    dpi=300
)

plt.close()

shutil.copy(
    "figures/lab10_csp_correlation.png",
    "docs/images/lab10_csp_correlation.png"
)

print("Correlation Figure Saved.")

# --------------------------------------------------
# Report
# --------------------------------------------------

with open(
    "results/lab10_04_csp_feature_analysis_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab10.4 - CSP Feature Analysis\n")
    report.write("="*50 + "\n\n")

    report.write(f"Samples : {df.shape[0]}\n")
    report.write(f"Features: {df.shape[1]}\n\n")

    report.write("Descriptive statistics generated.\n")
    report.write("Correlation matrix generated.\n")

print("Report Saved.")

print("\nLab10.4 Finished Successfully.")
