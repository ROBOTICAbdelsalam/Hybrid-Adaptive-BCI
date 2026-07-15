import os
import pandas as pd

print("=" * 60)
print("Lab14.7 - Real-Time System Final Report")
print("=" * 60)

# --------------------------------------------------
# Create Folder
# --------------------------------------------------

os.makedirs("realtime/results", exist_ok=True)

# --------------------------------------------------
# Files
# --------------------------------------------------

performance_file = "realtime/results/lab14_06_performance_summary.csv"
prediction_file = "realtime/results/realtime_predictions.csv"
command_file = "realtime/results/realtime_commands.csv"

# --------------------------------------------------
# Check Files
# --------------------------------------------------

if not os.path.exists(performance_file):
    print("Performance summary not found.")
    exit()

if not os.path.exists(prediction_file):
    print("Prediction results not found.")
    exit()

if not os.path.exists(command_file):
    print("Command results not found.")
    exit()

# --------------------------------------------------
# Load Files
# --------------------------------------------------

performance = pd.read_csv(performance_file)
predictions = pd.read_csv(prediction_file)
commands = pd.read_csv(command_file)

print("\nPerformance Summary")
print(performance)

# --------------------------------------------------
# Save Final Report
# --------------------------------------------------

report_file = "realtime/results/lab14_07_final_system_report.txt"

with open(report_file, "w", encoding="utf-8") as report:

    report.write("Chapter 14 - Real-Time BCI System Report\n")
    report.write("=" * 70 + "\n\n")

    report.write("SYSTEM OVERVIEW\n")
    report.write("-" * 70 + "\n")
    report.write("This report summarizes the complete real-time Brain-Computer\n")
    report.write("Interface pipeline developed in Chapter 14.\n\n")

    report.write("Completed Stages\n")
    report.write("------------------------------\n")
    report.write("1. Live EEG Streaming\n")
    report.write("2. Signal Preprocessing\n")
    report.write("3. Feature Extraction\n")
    report.write("4. Deep Learning Prediction\n")
    report.write("5. Decision Making\n")
    report.write("6. Performance Evaluation\n\n")

    report.write("PERFORMANCE SUMMARY\n")
    report.write("-" * 70 + "\n")
    report.write(performance.to_string(index=False))

    report.write("\n\nPREDICTION RESULTS\n")
    report.write("-" * 70 + "\n")
    report.write(predictions.to_string(index=False))

    report.write("\n\nGENERATED COMMANDS\n")
    report.write("-" * 70 + "\n")
    report.write(commands.to_string(index=False))

print("\nFinal Report Saved Successfully.")

print("\n============================================================")
print("Chapter 14 Completed Successfully")
print("============================================================")

print("\nFinal Report:")
print(report_file)

print("\nLab14.7 Finished Successfully.")