import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)

print("=" * 60)
print("Lab11.5 - Random Forest Classifier")
print("=" * 60)

# --------------------------------------------------
# Create Folders
# --------------------------------------------------

os.makedirs("models", exist_ok=True)
os.makedirs("results", exist_ok=True)
os.makedirs("figures", exist_ok=True)
os.makedirs("docs/images", exist_ok=True)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

X_train = pd.read_csv("ml_data/X_train.csv")
X_test = pd.read_csv("ml_data/X_test.csv")

y_train = pd.read_csv("ml_data/y_train.csv").squeeze()
y_test = pd.read_csv("ml_data/y_test.csv").squeeze()

print("Training Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# --------------------------------------------------
# Train Random Forest
# --------------------------------------------------

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

print("Random Forest Training Finished.")

# --------------------------------------------------
# Prediction
# --------------------------------------------------

y_pred = model.predict(X_test)

# --------------------------------------------------
# Metrics
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")

# --------------------------------------------------
# Classification Report
# --------------------------------------------------

report_text = classification_report(
    y_test,
    y_pred,
    zero_division=0
)

# --------------------------------------------------
# Confusion Matrix
# --------------------------------------------------

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)

disp.plot()

plt.title("Random Forest Confusion Matrix")

plt.savefig(
    "figures/lab11_random_forest_confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    "docs/images/lab11_random_forest_confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Confusion Matrix Saved.")

# --------------------------------------------------
# Save Model
# --------------------------------------------------

joblib.dump(
    model,
    "models/random_forest_classifier.pkl"
)

print("Model Saved.")

# --------------------------------------------------
# Save Report
# --------------------------------------------------

with open(
    "results/lab11_05_random_forest_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab11.5 - Random Forest Classifier\n")
    report.write("=" * 60 + "\n\n")

    report.write(f"Accuracy : {accuracy:.4f}\n")
    report.write(f"Precision: {precision:.4f}\n")
    report.write(f"Recall   : {recall:.4f}\n")
    report.write(f"F1 Score : {f1:.4f}\n\n")

    report.write("Classification Report\n")
    report.write("-" * 60 + "\n")
    report.write(report_text)

print("Report Saved.")
print("\nLab11.5 Finished Successfully.")