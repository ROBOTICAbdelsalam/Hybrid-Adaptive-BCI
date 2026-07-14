import os
import pandas as pd

print("=" * 60)
print("Lab13.2 - Adaptive Confidence Threshold")
print("=" * 60)

# --------------------------------------------------
# Create Folder
# --------------------------------------------------

os.makedirs("adaptive_ai", exist_ok=True)

feedback_file = "adaptive_ai/user_feedback.csv"

# --------------------------------------------------
# Check Feedback Database
# --------------------------------------------------

if not os.path.exists(feedback_file):

    print("Feedback database not found.")
    exit()

feedback = pd.read_csv(feedback_file)

print("\nFeedback Records :", len(feedback))

# --------------------------------------------------
# Statistics
# --------------------------------------------------

correct_predictions = feedback["Correct"].sum()

accuracy = correct_predictions / len(feedback)

print(f"Current Feedback Accuracy : {accuracy:.2f}")

# --------------------------------------------------
# Adaptive Threshold
# --------------------------------------------------

threshold = 0.80

if accuracy >= 0.90:

    threshold = 0.90

elif accuracy >= 0.75:

    threshold = 0.85

elif accuracy >= 0.60:

    threshold = 0.80

else:

    threshold = 0.70

print(f"\nNew Adaptive Threshold : {threshold:.2f}")

# --------------------------------------------------
# Save Threshold
# --------------------------------------------------

threshold_data = pd.DataFrame({

    "Feedback_Samples":[len(feedback)],

    "Feedback_Accuracy":[accuracy],

    "Adaptive_Threshold":[threshold]

})

threshold_data.to_csv(

    "adaptive_ai/adaptive_threshold.csv",

    index=False

)

print("\nAdaptive Threshold Saved Successfully.")

print("\nCurrent Threshold")

print(threshold_data)

print("\nLab13.2 Finished Successfully.")