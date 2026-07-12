import os
import shutil
import joblib

print("=" * 60)
print("Lab11.9 - Save Best Model")
print("=" * 60)

# --------------------------------------------------
# Create Folder
# --------------------------------------------------

os.makedirs("final_model", exist_ok=True)
os.makedirs("results", exist_ok=True)

# --------------------------------------------------
# Select Best Model
# --------------------------------------------------

best_model_name = "SVM"

source_model = "models/svm_classifier.pkl"
destination_model = "final_model/final_bci_model.pkl"

shutil.copy(source_model, destination_model)

print("Best Model :", best_model_name)
print("Model Copied Successfully.")

# --------------------------------------------------
# Copy Label Encoder (Optional)
# --------------------------------------------------

encoder_path = "models/xgboost_label_encoder.pkl"

if os.path.exists(encoder_path):
    shutil.copy(
        encoder_path,
        "final_model/label_encoder.pkl"
    )
    print("Label Encoder Copied.")

# --------------------------------------------------
# Save Metadata
# --------------------------------------------------

metadata = {
    "Model": best_model_name,
    "Accuracy": 0.8333,
    "Precision": 0.7083,
    "Recall": 0.8333,
    "F1 Score": 0.7619,
    "Dataset": "EEGBCI Subject 01 Run 04",
    "Feature Extraction": "Common Spatial Patterns (CSP)"
}

joblib.dump(
    metadata,
    "final_model/model_information.pkl"
)

# --------------------------------------------------
# Report
# --------------------------------------------------

with open(
    "results/lab11_09_final_model_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab11.9 - Final Model\n")
    report.write("=" * 60 + "\n\n")

    for key, value in metadata.items():
        report.write(f"{key}: {value}\n")

print("Metadata Saved.")
print("Report Saved.")

print("\nLab11.9 Finished Successfully.")