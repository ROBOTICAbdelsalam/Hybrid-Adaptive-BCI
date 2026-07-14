import os
import shutil

print("=" * 60)
print("Lab11.10 - Save CSP Model")
print("=" * 60)

# --------------------------------------------------
# Create Folders
# --------------------------------------------------

os.makedirs("models", exist_ok=True)
os.makedirs("results", exist_ok=True)

# --------------------------------------------------
# Source and Destination
# --------------------------------------------------

source = "csp/csp_model.pkl"
destination = "models/csp_model.pkl"

# --------------------------------------------------
# Check Source
# --------------------------------------------------

if not os.path.exists(source):
    print("\nERROR")
    print("CSP model not found.")
    exit()

# --------------------------------------------------
# Copy Model
# --------------------------------------------------

shutil.copy2(source, destination)

print("\nCSP Model Copied Successfully.")

# --------------------------------------------------
# Save Report
# --------------------------------------------------

with open(
    "results/lab11_10_csp_model_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab11.10 - Save CSP Model\n")
    report.write("=" * 60 + "\n\n")
    report.write(f"Source      : {source}\n")
    report.write(f"Destination : {destination}\n")

print("\nReport Saved.")

print("\nLab11.10 Finished Successfully.")