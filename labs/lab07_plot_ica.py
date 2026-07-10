
import os
import matplotlib.pyplot as plt
import mne
from mne.datasets import eegbci
from mne.preprocessing import ICA

print("=" * 50)
print("Lab 07.2 - ICA Components Visualization")
print("=" * 50)

# Load dataset
subject = 1
runs = [4]

files = eegbci.load_data(subject, runs)

raw = mne.io.read_raw_edf(files[0], preload=True)

# Rename channels
eegbci.standardize(raw)

# Set montage
montage = mne.channels.make_standard_montage("standard_1005")
raw.set_montage(montage)

# Band-pass filter
raw.filter(l_freq=1.0, h_freq=40.0)

# Train ICA
print("Training ICA...")
ica = ICA(
    n_components=20,
    random_state=42,
    method="fastica"
)

ica.fit(raw)

print("Generating ICA components...")

os.makedirs("figures", exist_ok=True)

figures = ica.plot_components(
    inst=raw,
    show=False
)

# Save every figure returned by MNE
if not isinstance(figures, list):
    figures = [figures]

for i, fig in enumerate(figures):
    filename = f"figures/lab07_ica_components_page_{i+1}.png"
    fig.savefig(
        filename,
        dpi=300,
        bbox_inches="tight"
    )
    plt.close(fig)
    print(f"Saved {filename}")

print("\nLab 07.2 completed successfully.")