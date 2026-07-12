import os
import joblib
import pandas as pd
import numpy as np
import mne
from mne.datasets import eegbci

print("="*60)
print("Lab10.2 - Train CSP")
print("="*60)

os.makedirs("csp", exist_ok=True)
os.makedirs("results", exist_ok=True)
# --------------------------------------------------
# Load Processed Epochs
# --------------------------------------------------

epochs = mne.read_epochs(
    "processed_data/subject01_run04-epo.fif",
    preload=True,
    verbose=False
)

X = epochs.get_data()

print("Epoch Shape :", X.shape)
# --------------------------------------------------
# Load CSP Model
# --------------------------------------------------

csp = joblib.load("csp/csp_model.pkl")

# --------------------------------------------------
# Transform EEG
# --------------------------------------------------

X_csp = csp.transform(X)

print("Original Shape :", X.shape)
print("CSP Shape      :", X_csp.shape)

# --------------------------------------------------
# Save CSP Features
# --------------------------------------------------

columns = [f"CSP_{i+1}" for i in range(X_csp.shape[1])]

df = pd.DataFrame(
    X_csp,
    columns=columns
)

df.to_csv(
    "csp/csp_features.csv",
    index=False
)

print("CSP Features Saved.")

# --------------------------------------------------
# Report
# --------------------------------------------------

with open(
    "results/lab10_02_train_csp_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab10.2 - Train CSP\n")
    report.write("="*50 + "\n\n")

    report.write(f"Original Shape : {X.shape}\n")
    report.write(f"CSP Shape      : {X_csp.shape}\n")
    report.write(f"Components     : {X_csp.shape[1]}\n")

print("Report Saved.")
print("\nLab10.2 Finished Successfully.")
