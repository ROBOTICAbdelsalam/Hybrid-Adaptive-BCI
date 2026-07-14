import os
import shutil
import pandas as pd

print("=" * 60)
print("Lab13.4 - Adaptive Classifier Update")
print("=" * 60)

# --------------------------------------------------
# Create Folders
# --------------------------------------------------

os.makedirs("adaptive_ai", exist_ok=True)
os.makedirs("models", exist_ok=True)
os.makedirs("results", exist_ok=True)

status_file = "adaptive_ai/online_learning_status.csv"
final_model = "models/final_deep_learning_model.keras"
updated_model = "models/adaptive_final_model.keras"

# --------------------------------------------------
# Check Files
# --------------------------------------------------

if not os.path.exists(status_file):
    print("Online learning status not found.")
    exit()

if not os.path.exists(final_model):
    print("Final Deep Learning model not found.")
    exit()

# --------------------------------------------------
# Load Status
# --------------------------------------------------

status = pd.read_csv(status_file)

samples = int(status.loc[0, "Feedback_Samples"])
accuracy = float(status.loc[0, "Feedback_Accuracy"])
threshold = float(status.loc[0, "Adaptive_Threshold"])
state = status.loc[0, "Status"]

print(f"\nFeedback Samples : {samples}")
print(f"Feedback Accuracy: {accuracy:.2f}")
print(f"Adaptive Threshold: {threshold:.2f}")
print(f"System Status: {state}")

# --------------------------------------------------
# Adaptive Update Decision
# --------------------------------------------------

if state == "READY":

    shutil.copy2(final_model, updated_model)

    update_status = "UPDATED"

    message = (
        "Adaptive classifier updated successfully."
    )

else:

    update_status = "WAITING"

    message = (
        "Insufficient feedback samples. "
        "Classifier update postponed."
    )

print("\nAdaptive Update")

print("----------------")

print(update_status)

print("\n" + message)

# --------------------------------------------------
# Save Update Information
# --------------------------------------------------

update_df = pd.DataFrame({

    "Feedback_Samples":[samples],

    "Feedback_Accuracy":[accuracy],

    "Adaptive_Threshold":[threshold],

    "Status":[state],

    "Update_Status":[update_status]

})

update_df.to_csv(

    "adaptive_ai/adaptive_update_status.csv",

    index=False

)

# --------------------------------------------------
# Save Report
# --------------------------------------------------

with open(

    "results/lab13_04_classifier_update_report.txt",

    "w",

    encoding="utf-8"

) as report:

    report.write("Lab13.4 - Adaptive Classifier Update\n")
    report.write("=" * 60 + "\n\n")

    report.write(f"Feedback Samples : {samples}\n")
    report.write(f"Feedback Accuracy: {accuracy:.2f}\n")
    report.write(f"Adaptive Threshold: {threshold:.2f}\n")
    report.write(f"System Status : {state}\n")
    report.write(f"Update Status : {update_status}\n\n")
    report.write(message)

print("\nUpdate Status Saved.")
print("Report Saved.")

print("\nLab13.4 Finished Successfully.")