import os
import pandas as pd

print("=" * 60)
print("Lab13.6 - Adaptive AI Final Report")
print("=" * 60)

# --------------------------------------------------
# Create Results Folder
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

required_files = [
    feedback_file,
    threshold_file,
    online_file,
    update_file
]

for file in required_files:

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

adaptation_score = round(
    accuracy * adaptive_threshold,
    4
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

        adaptation_score

    ]

})

print()

print(summary)

summary.to_csv(

    "results/lab13_06_adaptive_ai_summary.csv",

    index=False

)

# --------------------------------------------------
# Final Report
# --------------------------------------------------

with open(

    "results/lab13_06_final_adaptive_ai_report.txt",

    "w",

    encoding="utf-8"

) as report:

    report.write("Lab13.6 - Adaptive Artificial Intelligence Final Report\n")

    report.write("="*65 + "\n\n")

    report.write(summary.to_string(index=False))

    report.write("\n\n")

    report.write("System Assessment\n")

    report.write("-----------------------------\n")

    if update_status == "UPDATED":

        report.write(
            "The adaptive AI framework successfully updated the deployed classifier based on accumulated user feedback.\n"
        )

    else:

        report.write(
            "The adaptive AI framework is currently collecting additional user feedback before updating the deployed classifier.\n"
        )

    report.write("\n")

    report.write(
        "The proposed Adaptive AI framework integrates user feedback, adaptive confidence threshold adjustment, online learning, adaptive classifier update, and performance monitoring into a unified adaptive Brain–Computer Interface architecture."
    )

print("\nSummary Saved.")

print("Final Report Saved.")

print("\n============================================================")
print("Adaptive AI Final Summary")
print("============================================================")

print(f"Feedback Samples : {samples}")
print(f"Feedback Accuracy: {accuracy:.2f}")
print(f"Adaptive Threshold: {adaptive_threshold:.2f}")
print(f"Online Learning : {online_status}")
print(f"Classifier Update: {update_status}")
print(f"Adaptation Score : {adaptation_score:.2f}")

print("\nLab13.6 Finished Successfully.")