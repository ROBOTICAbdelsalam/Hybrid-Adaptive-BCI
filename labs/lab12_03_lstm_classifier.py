import os
import joblib
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
)

print("=" * 60)
print("Lab12.3 - LSTM Classifier")
print("=" * 60)

# --------------------------------------------------
# Create Folders
# --------------------------------------------------

os.makedirs("deep_learning", exist_ok=True)
os.makedirs("results", exist_ok=True)
os.makedirs("figures", exist_ok=True)
os.makedirs("docs/images", exist_ok=True)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

X_train = np.load("dl_data/X_train.npy")
X_test = np.load("dl_data/X_test.npy")

y_train = np.load("dl_data/y_train.npy")
y_test = np.load("dl_data/y_test.npy")

print("Training Shape :", X_train.shape)
print("Testing Shape  :", X_test.shape)

# --------------------------------------------------
# One-Hot Encoding
# --------------------------------------------------

num_classes = len(np.unique(y_train))

y_train_cat = to_categorical(y_train, num_classes)
y_test_cat = to_categorical(y_test, num_classes)

# --------------------------------------------------
# Build LSTM Model
# --------------------------------------------------

model = Sequential()

model.add(
    LSTM(
        64,
        input_shape=(X_train.shape[1], X_train.shape[2]),
        return_sequences=False
    )
)

model.add(Dropout(0.3))

model.add(Dense(32, activation="relu"))

model.add(Dense(num_classes, activation="softmax"))

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# --------------------------------------------------
# Train Model
# --------------------------------------------------

history = model.fit(
    X_train,
    y_train_cat,
    validation_data=(X_test, y_test_cat),
    epochs=50,
    batch_size=8,
    verbose=1
)

# --------------------------------------------------
# Prediction
# --------------------------------------------------

pred = model.predict(X_test)

pred = np.argmax(pred, axis=1)

accuracy = accuracy_score(y_test, pred)

precision = precision_score(
    y_test,
    pred,
    average="weighted",
    zero_division=0
)

recall = recall_score(
    y_test,
    pred,
    average="weighted",
    zero_division=0
)

f1 = f1_score(
    y_test,
    pred,
    average="weighted",
    zero_division=0
)

print("\nAccuracy :", round(accuracy,4))
print("Precision:", round(precision,4))
print("Recall   :", round(recall,4))
print("F1 Score :", round(f1,4))

# --------------------------------------------------
# Confusion Matrix
# --------------------------------------------------

cm = confusion_matrix(y_test, pred)

disp = ConfusionMatrixDisplay(cm)

disp.plot()

plt.savefig(
    "figures/lab12_lstm_confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    "docs/images/lab12_lstm_confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# --------------------------------------------------
# Accuracy Curve
# --------------------------------------------------

plt.figure(figsize=(7,5))

plt.plot(history.history["accuracy"], label="Training")
plt.plot(history.history["val_accuracy"], label="Validation")

plt.title("LSTM Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()

plt.savefig(
    "figures/lab12_lstm_accuracy.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    "docs/images/lab12_lstm_accuracy.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# --------------------------------------------------
# Loss Curve
# --------------------------------------------------

plt.figure(figsize=(7,5))

plt.plot(history.history["loss"], label="Training")
plt.plot(history.history["val_loss"], label="Validation")

plt.title("LSTM Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()

plt.savefig(
    "figures/lab12_lstm_loss.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    "docs/images/lab12_lstm_loss.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# --------------------------------------------------
# Save Model
# --------------------------------------------------

model.save("deep_learning/lstm_classifier.keras")

joblib.dump(
    history.history,
    "deep_learning/lstm_history.pkl"
)

# --------------------------------------------------
# Save Report
# --------------------------------------------------

with open(
    "results/lab12_03_lstm_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab12.3 - LSTM Classifier\n")
    report.write("=" * 60 + "\n\n")

    report.write(f"Training Samples : {X_train.shape[0]}\n")
    report.write(f"Testing Samples  : {X_test.shape[0]}\n\n")

    report.write(f"Accuracy : {accuracy:.4f}\n")
    report.write(f"Precision: {precision:.4f}\n")
    report.write(f"Recall   : {recall:.4f}\n")
    report.write(f"F1 Score : {f1:.4f}\n")

print("\nLSTM Model Saved.")
print("Training History Saved.")
print("Report Saved.")

print("\nLab12.3 Finished Successfully.")