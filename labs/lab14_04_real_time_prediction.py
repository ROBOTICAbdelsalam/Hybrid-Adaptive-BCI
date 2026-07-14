import os
import numpy as np
import pandas as pd
import tensorflow as tf

print("=" * 60)
print("Lab14.4 - Real-Time Prediction")
print("=" * 60)

# --------------------------------------------------
# Create Folder
# --------------------------------------------------

os.makedirs("realtime/results", exist_ok=True)

# --------------------------------------------------
# Files
# --------------------------------------------------

feature_file = "realtime/data/realtime_features.csv"
model_file = "models/final_deep_learning_model.keras"

# --------------------------------------------------
# Check Files
# --------------------------------------------------

if not os.path.exists(feature_file):
    print("Feature file not found.")
    exit()

if not os.path.exists(model_file):
    print("Model file not found.")
    exit()

# --------------------------------------------------
# Load Features
# --------------------------------------------------

features = pd.read_csv(feature_file)

print("\nFeature Matrix Shape:")
print(features.shape)

X = features.values.astype(np.float32)

# --------------------------------------------------
# Load Model
# --------------------------------------------------

model = tf.keras.models.load_model(model_file, compile=False)

print("\nModel Loaded Successfully.")

print("Model Input Shape :", model.input_shape)

expected_features = model.input_shape[1]

print("Expected Features :", expected_features)

if X.shape[1] != expected_features:

    raise ValueError(
        f"\nFeature mismatch.\n"
        f"Model expects {expected_features} features "
        f"but received {X.shape[1]}."
    )

# --------------------------------------------------
# Prepare Input
# --------------------------------------------------

X = X.reshape((X.shape[0], X.shape[1], 1))

print("\nPrediction Input Shape:")
print(X.shape)

# --------------------------------------------------
# Prediction
# --------------------------------------------------

predictions = model.predict(X, verbose=0)

predicted_class = np.argmax(predictions, axis=1)

confidence = np.max(predictions, axis=1)

# --------------------------------------------------
# Save Results
# --------------------------------------------------

results = pd.DataFrame({

    "Prediction": predicted_class,

    "Confidence": confidence

})

results.to_csv(
    "realtime/results/realtime_predictions.csv",
    index=False
)

print("\nPrediction Results")
print(results)

print("\nAverage Confidence")
print(round(confidence.mean(),4))

# --------------------------------------------------
# Save Report
# --------------------------------------------------

with open(
    "realtime/results/lab14_04_prediction_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab14.4 - Real-Time Prediction\n")
    report.write("=" * 60 + "\n\n")

    report.write(f"Input Shape : {X.shape}\n")
    report.write(f"Average Confidence : {confidence.mean():.4f}\n\n")

    report.write(results.to_string(index=False))

print("\nPrediction Report Saved.")

print("\nLab14.4 Finished Successfully.")