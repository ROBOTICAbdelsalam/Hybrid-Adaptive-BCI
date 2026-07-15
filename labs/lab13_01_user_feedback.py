import os
import pandas as pd
from datetime import datetime

print("=" * 60)
print("Lab13.1 - User Feedback Integration")
print("=" * 60)

# --------------------------------------------------
# Create Folder
# --------------------------------------------------

os.makedirs("adaptive_ai", exist_ok=True)

# --------------------------------------------------
# Simulated Prediction
# --------------------------------------------------

predicted_command = "Move Left"

confidence = 0.87

print(f"\nPredicted Command : {predicted_command}")
print(f"Confidence        : {confidence:.2f}")

# --------------------------------------------------
# Simulated User Feedback
# --------------------------------------------------

feedback = input(
    "\nWas the prediction correct? (yes/no): "
).strip().lower()

correct = feedback == "yes"

# --------------------------------------------------
# Save Feedback
# --------------------------------------------------

feedback_data = pd.DataFrame({

    "Timestamp":[
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ],

    "Predicted_Command":[
        predicted_command
    ],

    "Confidence":[
        confidence
    ],

    "User_Feedback":[
        feedback
    ],

    "Correct":[
        correct
    ]

})

file = "adaptive_ai/user_feedback.csv"

if os.path.exists(file):

    old = pd.read_csv(file)

    feedback_data = pd.concat(
        [old, feedback_data],
        ignore_index=True
    )

feedback_data.to_csv(
    file,
    index=False
)

print("\nFeedback Saved Successfully.")

print("\nCurrent Feedback Database\n")

print(feedback_data.tail())

print("\nLab13.1 Finished Successfully.")
# --------------------------------------------------
# Save Report
# --------------------------------------------------

with open(
    "results/lab13_01_user_feedback_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab13.1 - User Feedback Integration\n")
    report.write("=" * 60 + "\n\n")

    report.write(f"Predicted Command : {predicted_command}\n")
    report.write(f"Confidence        : {confidence:.2f}\n")
    report.write(f"User Feedback     : {feedback}\n")
    report.write(f"Correct           : {correct}\n")

print("Report Saved.")