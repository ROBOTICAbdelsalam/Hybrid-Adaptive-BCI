# Hybrid Adaptive BCI — Robotic Hand Control System

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![ROS2](https://img.shields.io/badge/ROS2-Jazzy-blue)
![Gazebo](https://img.shields.io/badge/Gazebo-Harmonic-orange)
![MoveIt2](https://img.shields.io/badge/MoveIt-2-green)
![Version](https://img.shields.io/badge/Release-v1.0-success)
![CI](https://github.com/ROBOTICAbdelsalam/Hybrid-Adaptive-BCI/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/License-MIT-yellow)

A Hybrid Brain–Computer Interface (BCI) with adaptive AI that turns EEG motor-imagery
into commands for a simulated **robotic hand**, through a **robot-independent** ROS2
architecture designed so industrial arms (Franka Panda, KUKA iiwa, UR5e) can be added
later without changing any EEG or AI code.

> Master's Thesis in Robotics — JAMK University of Applied Sciences, Finland.
> Author: **Mohamed Abdelsalam** · Supervisor: **Prof. Olli Väänänen**

---

## What this project is

The system is an end-to-end pipeline from brain signal to robot motion:

```
EEG  →  Preprocessing  →  Feature Extraction (CSP)  →  AI Model (CNN/LSTM)
     →  Real-Time Prediction  →  ROS2 Bridge  →  Robot Abstraction Layer
     →  Robotic Hand (Gazebo Harmonic + MoveIt2)
```

- **Labs 01–14** (Python) implement the neuroscience/AI half: EEG loading, filtering,
  ICA, epoching, feature extraction, Common Spatial Patterns, classical ML, deep
  learning, adaptive AI, and a real-time prediction/command pipeline.
- **`ros2_workspace/`** implements the robotics half: six ROS2 Jazzy packages providing
  the interface contract, a robot-independent abstraction layer, the AI→ROS2 bridge,
  the robotic-hand description + Gazebo simulation, MoveIt2 configuration, and a full
  bringup launch.

The two halves meet at one seam — the bridge reads the existing pipeline's output
files — so the AI code is never modified by the robotics code.

---

## Documentation

| Guide | Contents |
|-------|----------|
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | System architecture, data flow, robot-abstraction design, diagrams |
| [docs/USER_GUIDE.md](docs/USER_GUIDE.md) | Installation, build, run, ROS2 / Gazebo / MoveIt2 execution, testing, troubleshooting |
| [docs/PROJECT_REPORT.md](docs/PROJECT_REPORT.md) | Performance report, scientific validation, software-engineering & robotics summaries, future work |
| [ros2_workspace/README.md](ros2_workspace/README.md) | ROS2 workspace quick reference |
| `docs/Lab*.md` | Per-lab documentation for the EEG/AI pipeline |

---

## Repository structure

```text
Hybrid-Adaptive-BCI/
├── labs/                     # Labs 01–14: EEG → AI → real-time prediction (Python)
├── processed_data/           # Filtered + ICA-cleaned epochs (subject 1, run 4)
├── csp/                      # CSP models + features
├── ml_data/  dl_data/        # ML / DL train-test splits
├── models/  final_model/     # Trained SVM/RF/XGBoost/CNN-LSTM + deployed model
├── adaptive_ai/              # Adaptive threshold + feedback (Lab 13)
├── realtime/                 # Real-time streaming, prediction, command outputs (Lab 14)
├── results/  figures/        # Reports and plots
├── docs/                     # Documentation (guides + per-lab)
│
├── ros2_workspace/           # ROS2 Jazzy integration
│   ├── docker/               # Dockerfile + RunPod bootstrap + build/verify script
│   └── src/
│       ├── bci_interfaces/          # msgs/srv: robot-independent gesture contract
│       ├── bci_robot_abstraction/   # RobotInterface + registry + robot_node
│       ├── bci_bridge/              # AI predictions → ROS2 BCICommand
│       ├── bci_hand_description/     # URDF/Xacro + ros2_control + Gazebo launch
│       ├── bci_hand_moveit_config/  # MoveIt2 config + 6 named gesture states
│       └── bci_bringup/             # Hand adapter + full system launch
│
├── requirements.txt          # Python (AI pipeline) dependencies
├── requirements-ros2.txt     # ROS2 build tooling (installed via the ROS2 distro)
├── CHANGELOG.md  LICENSE
```

---

## Supported gestures

`REST` · `OPEN_HAND` · `CLOSE_HAND` · `PINCH_GRIP` · `POWER_GRIP` · `POINT`

Defined once in `bci_interfaces/msg/BCICommand.msg` and mapped per-robot by each
abstraction layer, so they are robot-independent by construction.

---

## Quick start

### 1. AI pipeline (macOS / Linux)

```bash
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python labs/lab14_04_real_time_prediction.py   # produces realtime/results/realtime_predictions.csv
```

### 2. Robotics (ROS2 Jazzy — Linux / RunPod)

```bash
bash ros2_workspace/docker/setup_runpod.sh      # ROS2 Jazzy + Gazebo Harmonic + MoveIt2
source /opt/ros/jazzy/setup.bash
cd ros2_workspace && bash docker/build_and_verify.sh
ros2 launch bci_bringup bci_system.launch.py    # EEG-predictions → robotic hand in Gazebo
```

Full details in [docs/USER_GUIDE.md](docs/USER_GUIDE.md).

---

## Technology stack

| Layer | Technology |
|-------|-----------|
| EEG / signal processing | MNE-Python, SciPy, NumPy |
| Feature extraction | Common Spatial Patterns (MNE) |
| Machine learning | scikit-learn, XGBoost |
| Deep learning | TensorFlow / Keras (CNN, LSTM, CNN-LSTM) |
| Robotics middleware | ROS2 Jazzy |
| Simulation | Gazebo Harmonic + `ros2_control` |
| Motion planning | MoveIt2 |

---

## Status

**v1.0 — complete.** EEG→AI→ROS2→robotic-hand pipeline implemented across six ROS2
packages plus the Labs 01–14 AI pipeline. The AI pipeline and all ROS2 package logic
are verified on the development host; `colcon build`, Gazebo and MoveIt2 runtime are
verified on a ROS2 Jazzy host (see [docs/PROJECT_REPORT.md](docs/PROJECT_REPORT.md)
for the full verification matrix).

---

## Author & license

**Mohamed Abdelsalam** — Master of Robotics, JAMK University of Applied Sciences.
Supervisor: **Prof. Olli Väänänen**. Released under the **MIT License** (see `LICENSE`).
