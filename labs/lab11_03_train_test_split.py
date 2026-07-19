import os
import joblib
import numpy as np
import pandas as pd
import mne
from mne.decoding import CSP
from sklearn.model_selection import train_test_split

print("=" * 60)
print("Lab11.3 - Train/Test Split")
print("=" * 60)

os.makedirs("ml_data", exist_ok=True)
os.makedirs("csp", exist_ok=True)
os.makedirs("results", exist_ok=True)

# --------------------------------------------------
# Load Processed Epochs
#
# The split is performed on the epochs, BEFORE CSP is
# fitted. CSP is a supervised transform, so fitting it
# on the full dataset (as in Lab 10) leaks test-set
# information into the training features. Splitting
# first keeps the test set unseen by CSP.
# --------------------------------------------------

epochs = mne.read_epochs(
    "processed_data/subject01_run04-epo.fif",
    preload=True,
    verbose=False
)

X = epochs.get_data(copy=True)
y = epochs.events[:, 2]

print("Epochs Loaded Successfully.")
print(f"Samples  : {X.shape[0]}")
print(f"Channels : {X.shape[1]}")

# --------------------------------------------------
# Train/Test Split (on epochs)
# --------------------------------------------------

X_train_epochs, X_test_epochs, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print(f"Training Samples : {len(y_train)}")
print(f"Testing Samples  : {len(y_test)}")

# --------------------------------------------------
# Fit CSP on Training Data Only
# --------------------------------------------------

csp = CSP(
    n_components=4,
    reg=None,
    log=True,
    norm_trace=False
)

X_train = csp.fit_transform(X_train_epochs, y_train)
X_test = csp.transform(X_test_epochs)

print(f"CSP Features     : {X_train.shape[1]}")

# --------------------------------------------------
# Save Feature Files
# --------------------------------------------------

columns = [f"CSP_{i + 1}" for i in range(X_train.shape[1])]

pd.DataFrame(X_train, columns=columns).to_csv(
    "ml_data/X_train.csv", index=False
)
pd.DataFrame(X_test, columns=columns).to_csv(
    "ml_data/X_test.csv", index=False
)

pd.Series(y_train, name="Label").to_csv(
    "ml_data/y_train.csv", index=False
)
pd.Series(y_test, name="Label").to_csv(
    "ml_data/y_test.csv", index=False
)

# --------------------------------------------------
# Save Leakage-Free CSP Model
# --------------------------------------------------

joblib.dump(csp, "csp/csp_model_train.pkl")

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

    report.write(f"Training Samples : {len(y_train)}\n")
    report.write(f"Testing Samples  : {len(y_test)}\n")
    report.write(f"CSP Features     : {X_train.shape[1]}\n")
    report.write("CSP fitted on training data only "
                 "(no test-set leakage).\n")

print("Train/Test Dataset Saved.")
print("Report Saved.")

print("\nLab11.3 Finished Successfully.")
