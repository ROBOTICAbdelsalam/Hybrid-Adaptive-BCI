# Changelog

All notable changes to this project will be documented in this file.

---

## Version 1.0.0 — Hybrid Adaptive BCI Robotic Hand System

First complete release: an end-to-end pipeline from EEG motor-imagery to a simulated
robotic hand, through a robot-independent ROS2 architecture.

### Scientific pipeline — corrections (branch `scientific-fixes`)

- **A4** — `processed_data/` now contains genuinely filtered + ICA-cleaned epochs
  (previously raw data saved under a "processed" name).
- **A2** — CSP is fit on the training split only; test-set leakage removed.
- **A3** — a stratified validation set is held out from training in all deep-learning
  labs; the test set is used only for final scoring.
- **A5** — adaptive confidence threshold direction corrected (low accuracy ⇒ more
  conservative gate) with a cold-start guard.
- **A1** — `requirements.txt` made reproducible: removed the invalid local wheel path,
  added all runtime dependencies, pinned versions (clean-room verified).

### ROS2 integration (branch `ros2-integration`)

- **Phase 1** — reproducible ROS2 Jazzy environment (Dockerfile + RunPod bootstrap +
  build/verify script) and `bci_interfaces` (robot-independent gesture contract).
- **Phase 2** — `bci_robot_abstraction` (RobotInterface + registry + `robot_node`) and
  `bci_bridge` (consumes existing Lab 13/14 outputs, publishes `BCICommand`).
- **Phase 3** — `bci_hand_description`: five-finger hand URDF/Xacro, `ros2_control`,
  Gazebo Harmonic launch.
- **Phase 4** — `bci_hand_moveit_config`: MoveIt2 planning group + six named gesture
  states, with a cross-package consistency test.
- **Phase 5** — `bci_bringup`: hand trajectory adapter + full-system launch
  (EEG predictions → bridge → abstraction → hand → Gazebo).

### Release engineering

- All six ROS2 packages versioned 1.0.0.
- 33 unit/structural tests; AI pipeline smoke-tested; URDF/SRDF consistency verified.
- Documentation set: README, ARCHITECTURE, USER_GUIDE, PROJECT_REPORT.
- Removed stray placeholder directories and dead code.

### Verified

- AI pipeline (CSP + deployed model), all pure-logic and structural tests on the dev
  host. `colcon build`, Gazebo and MoveIt2 runtime on a ROS2 Jazzy host — see the
  verification matrix in `docs/PROJECT_REPORT.md`.

---

## Version 0.7.0

### Added

- Project structure, README, GitHub badges, MIT License, requirements, .gitignore.

### Completed Laboratories

- Labs 01–07: environment setup, EEG loading, EDF reading, visualization, dataset
  inspection, filtering, and the full ICA artifact-removal sub-labs (07.1–07.7).
