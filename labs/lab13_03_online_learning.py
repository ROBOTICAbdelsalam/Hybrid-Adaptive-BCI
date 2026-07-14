import os
import pandas as pd

print("=" * 60)
print("Lab13.3 - Online Learning")
print("=" * 60)

# --------------------------------------------------
# Create Folder
# --------------------------------------------------

os.makedirs("adaptive_ai", exist_ok=True)

feedback_file = "adaptive_ai/user_feedback.csv"
threshold_file = "adaptive_ai/adaptive_threshold.csv"

# --------------------------------------------------
# Check Files
# --------------------------------------------------

if not os.path.exists(feedback_file):
    print("User feedback database not found.")
    exit()

if not os.path.exists(threshold_file):
    print("Adaptive threshold file not found.")
    exit()

# --------------------------------------------------
# Load Data
# --------------------------------------------------

feedback = pd.read_csv(feedback_file)
threshold = pd.read_csv(threshold_file)

samples = len(feedback)

accuracy = feedback["Correct"].mean()

current_threshold = threshold.loc[0, "Adaptive_Threshold"]

print(f"\nFeedback Samples : {samples}")
print(f"Feedback Accuracy: {accuracy:.2f}")
print(f"Current Threshold: {current_threshold:.2f}")

# --------------------------------------------------
# Online Learning Decision
# --------------------------------------------------

minimum_samples = 10

if samples >= minimum_samples:

    status = "READY"

    message = (
        "Sufficient feedback collected. "
        "The classifier can now be updated."
    )

else:

    status = "WAITING"

    remaining = minimum_samples - samples

    message = (
        f"Collect {remaining} more feedback samples "
        "before updating the classifier."
    )

print("\nOnline Learning Status")

print("----------------------")

print(status)

print("\n" + message)

# --------------------------------------------------
# Save Status
# --------------------------------------------------

status_df = pd.DataFrame({

    "Feedback_Samples":[samples],

    "Feedback_Accuracy":[accuracy],

    "Adaptive_Threshold":[current_threshold],

    "Minimum_Samples":[minimum_samples],

    "Status":[status]

})

status_df.to_csv(

    "adaptive_ai/online_learning_status.csv",

    index=False

)

# --------------------------------------------------
# Report
# --------------------------------------------------

with open(

    "results/lab13_03_online_learning_report.txt",

    "w",

    encoding="utf-8"

) as report:

    report.write("Lab13.3 - Online Learning\n")

    report.write("="*60 + "\n\n")

    report.write(f"Feedback Samples : {samples}\n")

    report.write(f"Feedback Accuracy: {accuracy:.2f}\n")

    report.write(f"Adaptive Threshold: {current_threshold:.2f}\n")

    report.write(f"Status : {status}\n\n")

    report.write(message)

print("\nStatus Saved.")

print("Report Saved.")

print("\nLab13.3 Finished Successfully.")