import os
import pandas as pd
from sklearn.model_selection import train_test_split

print("=" * 60)
print("Lab11.3 - Train/Test Split")
print("=" * 60)

os.makedirs("ml_data", exist_ok=True)
os.makedirs("results", exist_ok=True)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

dataset = pd.read_csv("csp/csp_dataset_with_labels.csv")

X = dataset.drop(columns=["Label"])
y = dataset["Label"]

print("Dataset Loaded Successfully.")
print(f"Samples  : {len(dataset)}")
print(f"Features : {X.shape[1]}")

# --------------------------------------------------
# Train/Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print(f"Training Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")

# --------------------------------------------------
# Save Files
# --------------------------------------------------

X_train.to_csv("ml_data/X_train.csv", index=False)
X_test.to_csv("ml_data/X_test.csv", index=False)

y_train.to_csv("ml_data/y_train.csv", index=False)
y_test.to_csv("ml_data/y_test.csv", index=False)

# --------------------------------------------------
# Report
# --------------------------------------------------

with open(
    "results/lab11_03_train_test_split_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab11.3 - Train/Test Split\n")
    report.write("=" * 55 + "\n\n")

    report.write(f"Training Samples : {len(X_train)}\n")
    report.write(f"Testing Samples  : {len(X_test)}\n")
    report.write(f"Features         : {X.shape[1]}\n")

print("Train/Test Dataset Saved.")
print("Report Saved.")

print("\nLab11.3 Finished Successfully.")
