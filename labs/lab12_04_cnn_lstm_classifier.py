import os
import joblib
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Input,
    Conv1D,
    MaxPooling1D,
    LSTM,
    Dense,
    Dropout
)

from tensorflow.keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint,
    ReduceLROnPlateau
)

from tensorflow.keras.utils import to_categorical

from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)

print("="*60)
print("Lab12.4 - CNN-LSTM Hybrid Classifier")
print("="*60)

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

num_classes = len(np.unique(y_train))

# --------------------------------------------------
# Validation Split
#
# The validation set is held out from the training
# data so that the test set is never seen during
# training or model selection.
# --------------------------------------------------

X_train, X_val, y_train, y_val = train_test_split(
    X_train,
    y_train,
    test_size=0.20,
    random_state=42,
    stratify=y_train
)

y_train_cat = to_categorical(y_train, num_classes)
y_val_cat = to_categorical(y_val, num_classes)
y_test_cat = to_categorical(y_test, num_classes)

print("Training Shape   :", X_train.shape)
print("Validation Shape :", X_val.shape)
print("Testing Shape    :", X_test.shape)

# --------------------------------------------------
# CNN-LSTM Model
# --------------------------------------------------

model = Sequential([

    Input(shape=(X_train.shape[1], X_train.shape[2])),

    Conv1D(
        filters=32,
        kernel_size=2,
        activation="relu"
    ),

    MaxPooling1D(pool_size=2),

    LSTM(64),

    Dropout(0.3),

    Dense(
        32,
        activation="relu"
    ),

    Dense(
        num_classes,
        activation="softmax"
    )
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# --------------------------------------------------
# Callbacks
# --------------------------------------------------

early_stop = EarlyStopping(
    monitor="val_loss",
    patience=10,
    restore_best_weights=True
)

checkpoint = ModelCheckpoint(
    "deep_learning/cnn_lstm_best.keras",
    save_best_only=True,
    monitor="val_accuracy"
)

reduce_lr = ReduceLROnPlateau(
    monitor="val_loss",
    factor=0.5,
    patience=5,
    verbose=1
)

# --------------------------------------------------
# Training
# --------------------------------------------------

history = model.fit(

    X_train,
    y_train_cat,

    validation_data=(X_val, y_val_cat),

    epochs=100,

    batch_size=8,

    callbacks=[
        early_stop,
        checkpoint,
        reduce_lr
    ],

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

print("\nAccuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)
print("F1 Score :", f1)

print("\nClassification Report\n")

print(
    classification_report(
        y_test,
        pred,
        zero_division=0
    )
)

# --------------------------------------------------
# Confusion Matrix
# --------------------------------------------------

cm = confusion_matrix(
    y_test,
    pred
)

disp = ConfusionMatrixDisplay(cm)

disp.plot()

plt.savefig(
    "figures/lab12_cnn_lstm_confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    "docs/images/lab12_cnn_lstm_confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# --------------------------------------------------
# Accuracy Curve
# --------------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(history.history["accuracy"], label="Training")

plt.plot(history.history["val_accuracy"], label="Validation")

plt.title("CNN-LSTM Accuracy")

plt.xlabel("Epoch")

plt.ylabel("Accuracy")

plt.legend()

plt.savefig(
    "figures/lab12_cnn_lstm_accuracy.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# --------------------------------------------------
# Loss Curve
# --------------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(history.history["loss"], label="Training")

plt.plot(history.history["val_loss"], label="Validation")

plt.title("CNN-LSTM Loss")

plt.xlabel("Epoch")

plt.ylabel("Loss")

plt.legend()

plt.savefig(
    "figures/lab12_cnn_lstm_loss.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# --------------------------------------------------
# Save
# --------------------------------------------------

model.save(
    "deep_learning/cnn_lstm_classifier.keras"
)

joblib.dump(
    history.history,
    "deep_learning/cnn_lstm_history.pkl"
)

# --------------------------------------------------
# Report
# --------------------------------------------------

with open(
    "results/lab12_04_cnn_lstm_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write("Lab12.4 - CNN-LSTM Hybrid\n")
    report.write("="*60 + "\n\n")

    report.write(f"Accuracy : {accuracy:.4f}\n")
    report.write(f"Precision: {precision:.4f}\n")
    report.write(f"Recall   : {recall:.4f}\n")
    report.write(f"F1 Score : {f1:.4f}\n")

print("\nBest Model Saved.")
print("Report Saved.")

print("\nLab12.4 Finished Successfully.")