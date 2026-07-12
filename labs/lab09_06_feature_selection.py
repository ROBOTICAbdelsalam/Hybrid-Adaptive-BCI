import os
import pandas as pd
from sklearn.feature_selection import VarianceThreshold

print("=" * 60)
print("Lab09.6 - Feature Selection")
print("=" * 60)

os.makedirs("results", exist_ok=True)
os.makedirs("features", exist_ok=True)

# --------------------------------------------------
# Load Feature Files
# --------------------------------------------------

time_df = pd.read_csv("features/time_domain_features.csv").add_prefix("TD_")
freq_df = pd.read_csv("features/frequency_domain_features.csv").add_prefix("FD_")
psd_df = pd.read_csv("features/psd_features.csv").add_prefix("PSD_")
band_df = pd.read_csv("features/band_power_features.csv").add_prefix("BP_")
stat_df = pd.read_csv("features/statistical_features.csv").add_prefix("STAT_")

# --------------------------------------------------
# Merge All Features
# --------------------------------------------------

all_features = pd.concat(
    [time_df, freq_df, psd_df, band_df, stat_df],
    axis=1
)

print(f"Original Feature Matrix : {all_features.shape}")

# --------------------------------------------------
# Variance Threshold
# --------------------------------------------------

selector = VarianceThreshold(threshold=1e-12)

selected = selector.fit_transform(all_features)

selected_columns = all_features.columns[selector.get_support()]

final_df = pd.DataFrame(
    selected,
    columns=selected_columns
)

print(f"Selected Feature Matrix : {final_df.shape}")

# --------------------------------------------------
# Save Final Feature Matrix
# --------------------------------------------------

output_file = "features/final_feature_matrix.csv"

final_df.to_csv(output_file, index=False)

print("Final Feature Matrix Saved.")

# --------------------------------------------------
# Report
# --------------------------------------------------

with open(
    "results/lab09_06_feature_selection_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab09.6 - Feature Selection\n")
    report.write("=" * 50 + "\n\n")

    report.write(f"Original Features : {all_features.shape[1]}\n")
    report.write(f"Selected Features : {final_df.shape[1]}\n")
    report.write(f"Epochs            : {final_df.shape[0]}\n")

print("Report Saved.")
print("\nLab09.6 Finished Successfully.")
