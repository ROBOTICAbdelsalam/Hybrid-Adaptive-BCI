import os
import pandas as pd

print("=" * 60)
print("Lab14.5 - Real-Time Decision Making")
print("=" * 60)

# --------------------------------------------------
# Create Folder
# --------------------------------------------------

os.makedirs("realtime/results", exist_ok=True)

# --------------------------------------------------
# Load Predictions
# --------------------------------------------------

prediction_file = "realtime/results/realtime_predictions.csv"

if not os.path.exists(prediction_file):
    print("Prediction file not found.")
    exit()

predictions = pd.read_csv(prediction_file)

print("\nPrediction Results")
print(predictions)

# --------------------------------------------------
# Confidence Threshold
# --------------------------------------------------

CONFIDENCE_THRESHOLD = 0.75

print(f"\nConfidence Threshold : {CONFIDENCE_THRESHOLD}")

# --------------------------------------------------
# Command Mapping
# --------------------------------------------------

command_map = {
    0: "STOP",
    1: "LEFT",
    2: "RIGHT"
}

commands = []

for _, row in predictions.iterrows():

    prediction = int(row["Prediction"])
    confidence = float(row["Confidence"])

    if confidence >= CONFIDENCE_THRESHOLD:
        command = command_map.get(prediction, "UNKNOWN")
    else:
        command = "NO ACTION"

    commands.append(command)

predictions["Command"] = commands

# --------------------------------------------------
# Save Commands
# --------------------------------------------------

output_file = "realtime/results/realtime_commands.csv"

predictions.to_csv(
    output_file,
    index=False
)

print("\nGenerated Commands")
print(predictions)

# --------------------------------------------------
# Statistics
# --------------------------------------------------

print("\nCommand Statistics")
print(predictions["Command"].value_counts())

# --------------------------------------------------
# Save Report
# --------------------------------------------------

report_file = "realtime/results/lab14_05_command_report.txt"

with open(report_file, "w", encoding="utf-8") as report:

    report.write("Lab14.5 - Real-Time Decision Making\n")
    report.write("=" * 60 + "\n\n")

    report.write(f"Confidence Threshold : {CONFIDENCE_THRESHOLD}\n\n")

    report.write(predictions.to_string(index=False))

print("\nReport Saved.")

print("\nLab14.5 Finished Successfully.")