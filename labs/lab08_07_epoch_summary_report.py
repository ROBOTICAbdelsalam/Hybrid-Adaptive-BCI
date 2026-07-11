import os

print("=" * 60)
print("Lab 08.7 - Epoch Summary Report")
print("=" * 60)

os.makedirs("results", exist_ok=True)

summary = """
Lab 08 - Epoch Processing Summary
==================================================

Dataset
-------
EEG Motor Movement / Imagery Dataset (EEGBCI)

Subject : 1
Run     : 4

Processing Pipeline
-------------------
✓ Lab08.1 Event Extraction
✓ Lab08.2 Epoch Creation
✓ Lab08.3 Baseline Correction
✓ Lab08.4 Epoch Visualization
✓ Lab08.5 Epoch Quality Check
✓ Lab08.6 Save Processed Epochs

Results
-------
Detected Events : 30
Valid Epochs    : 29
Epoch Shape     : (29, 64, 161)

Generated Files
---------------
lab08_01_event_extraction_report.txt
lab08_02_epoch_creation_report.txt
lab08_03_baseline_correction_report.txt
lab08_04_epoch_visualization_report.txt
lab08_05_epoch_quality_check_report.txt
lab08_06_save_processed_epochs_report.txt

Conclusion
----------
Epoch preprocessing has been completed successfully.
The processed EEG data are now ready for Feature Extraction (Lab09).

"""

with open(
    "results/lab08_07_epoch_summary_report.txt",
    "w",
    encoding="utf-8"
) as report:
    report.write(summary)

print(summary)

print("Summary report saved successfully.")
print("\nLab08 Completed Successfully.")
