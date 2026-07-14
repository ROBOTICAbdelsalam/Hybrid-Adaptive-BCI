import os
import pandas as pd

print("=" * 60)
print("Lab13.5 - Performance Adaptation")
print("=" * 60)

# --------------------------------------------------
# Create Folder
# --------------------------------------------------

os.makedirs("results", exist_ok=True)

# --------------------------------------------------
# Files
# --------------------------------------------------

feedback_file = "adaptive_ai/user_feedback.csv"
threshold_file = "adaptive_ai/adaptive_threshold.csv"
online_file = "adaptive_ai/online_learning_status.csv"
update_file = "adaptive_ai/adaptive_update_status.csv"

# --------------------------------------------------
# Check Files
# --------------------------------------------------

for file in [feedback_file, threshold_file, online_file, update_file]:

    if not os.path.exists(file):
        print(f"Missing file: {file}")
        exit()

# --------------------------------------------------
# Load Data
# --------------------------------------------------

feedback = pd.read_csv(feedback_file)
threshold = pd.read_csv(threshold_file)
online = pd.read_csv(online_file)
update = pd.read_csv(update_file)

# --------------------------------------------------
# Statistics
# --------------------------------------------------

samples = len(feedback)

accuracy = feedback["Correct"].mean()

adaptive_threshold = threshold.loc[0, "Adaptive_Threshold"]

online_status = online.loc[0, "Status"]

update_status = update.loc[0, "Update_Status"]

adaptation_score = (
    accuracy * adaptive_threshold
)

# --------------------------------------------------
# Summary Table
# --------------------------------------------------

summary = pd.DataFrame({

    "Metric":[
        "Feedback Samples",
        "Feedback Accuracy",
        "Adaptive Threshold",
        "Online Learning",
        "Classifier Update",
        "Adaptation Score"
    ],

    "Value":[
        samples,
        round(accuracy,4),
        adaptive_threshold,
        online_status,
        update_status,
        round(adaptation_score,4)
    ]

})

print()

print(summary)

summary.to_csv(

    "results/lab13_05_performance_summary.csv",

    index=False

)

# --------------------------------------------------
# Final Report
# --------------------------------------------------

with open(

    "results/lab13_05_performance_adaptation_report.txt",

    "w",

    encoding="utf-8"

) as report:

    report.write("Lab13.5 - Performance Adaptation\n")

    report.write("="*60 + "\n\n")

    report.write(summary.to_string(index=False))

    report.write("\n\n")

    report.write("System Analysis\n")
    report.write("-----------------------------\n")

    if update_status == "UPDATED":

        report.write(
            "The adaptive system successfully updated the classifier.\n"
        )

    else:

        report.write(
            "The adaptive system is collecting more feedback before updating the classifier.\n"
        )

print("\nPerformance Summary Saved.")

print("Performance Report Saved.")

print("\nLab13.5 Finished Successfully.")