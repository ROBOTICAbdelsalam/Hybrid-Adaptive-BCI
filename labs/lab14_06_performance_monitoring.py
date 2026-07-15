import os
import pandas as pd

print("=" * 60)
print("Lab14.6 - Real-Time System Evaluation")
print("=" * 60)

# --------------------------------------------------
# Create Folder
# --------------------------------------------------

os.makedirs("realtime/results", exist_ok=True)

# --------------------------------------------------
# Load Commands
# --------------------------------------------------

command_file = "realtime/results/realtime_commands.csv"

if not os.path.exists(command_file):
    print("Command file not found.")
    exit()

data = pd.read_csv(command_file)

print("\nLoaded Commands")
print(data)

# --------------------------------------------------
# Performance Metrics
# --------------------------------------------------

total_predictions = len(data)

executed_commands = (data["Command"] != "NO ACTION").sum()

rejected_commands = (data["Command"] == "NO ACTION").sum()

execution_rate = (executed_commands / total_predictions) * 100

average_confidence = data["Confidence"].mean()

maximum_confidence = data["Confidence"].max()

minimum_confidence = data["Confidence"].min()

# --------------------------------------------------
# Summary
# --------------------------------------------------

summary = pd.DataFrame({

    "Metric": [

        "Total Predictions",
        "Executed Commands",
        "Rejected Commands",
        "Execution Rate (%)",
        "Average Confidence",
        "Maximum Confidence",
        "Minimum Confidence"

    ],

    "Value": [

        total_predictions,
        executed_commands,
        rejected_commands,
        round(execution_rate,2),
        round(average_confidence,4),
        round(maximum_confidence,4),
        round(minimum_confidence,4)

    ]

})

print("\nPerformance Summary")
print(summary)

# --------------------------------------------------
# Save Summary
# --------------------------------------------------

summary.to_csv(

    "realtime/results/lab14_06_performance_summary.csv",

    index=False

)

# --------------------------------------------------
# Save Report
# --------------------------------------------------

with open(

    "realtime/results/lab14_06_performance_report.txt",

    "w",

    encoding="utf-8"

) as report:

    report.write("Lab14.6 - Real-Time System Evaluation\n")

    report.write("=" * 60 + "\n\n")

    report.write(summary.to_string(index=False))

print("\nPerformance Summary Saved.")
print("Performance Report Saved.")

print("\n============================================================")
print("Real-Time Performance")
print("============================================================")

print(f"Total Predictions   : {total_predictions}")
print(f"Executed Commands   : {executed_commands}")
print(f"Rejected Commands   : {rejected_commands}")
print(f"Execution Rate (%)  : {execution_rate:.2f}")
print(f"Average Confidence  : {average_confidence:.4f}")

print("\nLab14.6 Finished Successfully.")