# BCI ROS2 Workspace

ROS2 integration for the Hybrid Adaptive BCI. It bridges the existing EEG /
AI real-time pipeline (Labs 01–14) to a simulated **Robotic Hand**, through a
**robot-independent** architecture so that industrial arms (Franka Panda,
KUKA iiwa, UR5e) can be added later without changing any EEG or AI code.

```
EEG → Preprocessing → Feature Extraction → AI Model → Real-Time Prediction
                                                            │
                                                            ▼
                                                      ROS2 Bridge
                                                            │
                                                            ▼
                                                Robot Abstraction Layer
                                                            │
                                                            ▼
                                                     Robotic Hand
```

## Target stack

| Component | Version |
|-----------|---------|
| ROS2      | Jazzy Jalisco (Ubuntu 24.04) |
| Simulator | Gazebo Harmonic |
| Planning  | MoveIt2 |

ROS2 Jazzy is Linux-only. This workspace is developed on macOS but **built and
verified on a rented RunPod Ubuntu 24.04 instance**.

## Build & verify on RunPod

Start a pod from the provided Docker image, or bootstrap a stock Ubuntu 24.04
pod:

```bash
# Option A — provided image (reproducible)
docker build -t bci-ros2:jazzy -f docker/Dockerfile .
docker run -it --rm bci-ros2:jazzy

# Option B — bootstrap a bare Ubuntu 24.04 pod
bash ros2_workspace/docker/setup_runpod.sh

# Then, in the workspace:
bash docker/build_and_verify.sh
```

`build_and_verify.sh` runs `colcon build` and confirms the generated
interfaces resolve — the per-phase "build, run, verify" loop.

## Packages

| Package | Type | Purpose |
|---------|------|---------|
| `bci_interfaces` | ament_cmake | Robot-independent gesture messages/services (the contract) |

*(further packages — abstraction layer, bridge, hand description, bringup —
are added in subsequent phases.)*

## Supported gestures

`REST`, `OPEN_HAND`, `CLOSE_HAND`, `PINCH_GRIP`, `POWER_GRIP`, `POINT` —
defined once in `bci_interfaces/msg/BCICommand.msg` and mapped per-robot by
each abstraction layer.
