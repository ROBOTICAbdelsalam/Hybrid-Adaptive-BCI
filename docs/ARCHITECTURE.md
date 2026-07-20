# Architecture — Hybrid Adaptive BCI Robotic Hand System (v1.0)

## 1. Overview

The system is a layered pipeline from EEG signal to robot motion. Each layer has a
single responsibility and a well-defined interface to the next, so layers can be
tested, replaced or extended independently. The central design goal is
**robot-independence**: everything above the robot abstraction layer speaks only in
semantic *gestures*, never in joints or hardware.

```
┌──────────────────────────────────────────────────────────────────────┐
│  AI PIPELINE  (Labs 01–14, Python — unchanged by the robotics layer)   │
│                                                                        │
│  EEG acquisition ─► preprocessing ─► CSP features ─► CNN/LSTM model     │
│        (MNE)          (filter+ICA)     (spatial)      (TensorFlow)      │
│                                                          │             │
│                              adaptive threshold ◄────────┤ prediction  │
│                              (Lab 13)                     ▼             │
│                                          realtime_predictions.csv       │
└────────────────────────────────────────────────┬───────────────────────┘
                                                  │  (file seam — no code coupling)
┌─────────────────────────────────────────────────▼──────────────────────┐
│  ROS2 INTEGRATION  (ros2_workspace, ROS2 Jazzy)                          │
│                                                                         │
│  bci_bridge ──►  /bci/command  (BCICommand: gesture + confidence)        │
│      │                                                                  │
│      ▼                                                                  │
│  bci_robot_abstraction (robot_node, registry-selected robot)            │
│      │   /bci/robot_state (feedback)                                     │
│      ▼   /bci/joint_targets (normalised)                                 │
│  bci_bringup (hand_trajectory_adapter)                                   │
│      │   /hand_controller/joint_trajectory (radians)                     │
│      ▼                                                                  │
│  ros2_control ──► Gazebo Harmonic robotic hand   (+ MoveIt2 planning)    │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Component responsibilities

| Component | Package | Responsibility |
|-----------|---------|----------------|
| Interface contract | `bci_interfaces` | `BCICommand`, `RobotState` msgs + `ExecuteGesture` srv — the robot-independent vocabulary |
| AI→ROS2 bridge | `bci_bridge` | Read Lab 13/14 outputs, gate by confidence, publish `BCICommand` |
| Robot abstraction | `bci_robot_abstraction` | `RobotInterface` contract, gesture library, registry, `robot_node` |
| Hand description | `bci_hand_description` | URDF/Xacro, `ros2_control`, Gazebo launch |
| MoveIt2 config | `bci_hand_moveit_config` | Planning group + 6 named gesture states |
| Bringup | `bci_bringup` | Hand trajectory adapter + full-system launch |

## 3. The robot-independence seam

The key architectural decision is *where* robot-specific knowledge is allowed to live.

- **Above `/bci/command`** everything is semantic: a gesture id (`OPEN_HAND`) plus a
  confidence. The AI pipeline and the bridge never know what a "hand" is.
- **`robot_node`** picks a concrete robot from a **registry** via a single
  `robot_type` parameter. It calls `RobotInterface.execute_gesture()` and publishes
  the resulting normalised joint targets. It still does not contain hand-specific code.
- **`hand_trajectory_adapter`** (in `bci_bringup`) is the *only* place that knows the
  hand's radian range and controller topic. An industrial arm would supply its own
  adapter and its own `RobotInterface` subclass.

Adding a new robot is therefore three additive changes and **zero** edits to the AI
pipeline, the bridge, or the interface contract:

```python
# 1. implement the contract
class UR5eArm(RobotInterface): ...
# 2. register it
_REGISTRY = {"robotic_hand": RoboticHand, "ur5e": UR5eArm}
# 3. select it at launch
ros2 launch bci_bringup bci_system.launch.py   # robot_type:=ur5e (+ its adapter)
```

## 4. Testability by design

The decision logic is deliberately kept in **pure Python modules with no ROS2
imports**, wrapped by thin `rclpy` nodes:

| Pure (unit-tested off-ROS) | ROS2 wrapper (transport only) |
|----------------------------|-------------------------------|
| `gesture_library`, `robot_interface`, `robotic_hand_interface`, `robot_registry` | `robot_node` |
| `prediction_source` | `bridge_node` |
| `scaling` | `trajectory_adapter` |

This is why 33 unit/structural tests run on a plain Python host with no ROS2
installed, and why the gesture definitions are provably consistent across the
abstraction, the URDF and the MoveIt SRDF (see `bci_hand_moveit_config/test`).

## 5. Single source of truth for gestures

The six gestures are defined once and bound together by tests:

```
BCICommand.msg constants  ══  gesture_library.GESTURES        (id ↔ name)
robotic_hand_interface    ══  normalised finger poses [0,1]
URDF joint limit (1.4 rad) ×  normalised pose   ══  SRDF named state (rad)
```

`bci_hand_moveit_config/test/test_named_states.py` enforces the last relationship, so
a gesture cannot drift between the abstraction, the robot description and the planner.

## 6. Topic / service interface

| Name | Type | Producer → Consumer |
|------|------|---------------------|
| `/bci/command` | `bci_interfaces/BCICommand` | bridge → robot_node |
| `/bci/robot_state` | `bci_interfaces/RobotState` | robot_node → (monitors) |
| `/bci/joint_targets` | `std_msgs/Float64MultiArray` | robot_node → hand adapter |
| `/bci/execute_gesture` | `bci_interfaces/ExecuteGesture` | any client → robot_node |
| `/hand_controller/joint_trajectory` | `trajectory_msgs/JointTrajectory` | hand adapter → ros2_control |
