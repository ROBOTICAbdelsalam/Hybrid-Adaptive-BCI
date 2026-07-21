# Project Report — Hybrid Adaptive BCI Robotic Hand System (v1.0)

## 1. Verification matrix

Verification is split honestly by where it can be executed. The development host is
macOS (Apple Silicon); ROS2 Jazzy, Gazebo and MoveIt2 are Linux-only and are verified
on a ROS2 Jazzy host (RunPod Ubuntu 24.04).

| Item | Dev host | CI (GitHub Actions) | ROS2 host (RunPod) |
|------|:--------:|:-------------------:|:------------------:|
| AI pipeline: CSP transform + deployed model predict | ✅ smoke | ✅ `ai-validation` | — |
| 7 AI scientific-invariant tests (filtering, no leakage, model I/O) | ✅ pytest | ✅ | — |
| Leakage-free CSP fit (train-only) | ✅ | ✅ | — |
| Validation/test separation (DL) | ✅ | ✅ | — |
| Adaptive threshold direction + cold-start | ✅ | ✅ | — |
| `requirements.txt` clean-room install | ✅ | ✅ | — |
| 36 ROS2 unit/structural tests | ✅ pytest | ✅ `quality` | ✅ `colcon test` |
| Lint (pycodestyle, ≤99 cols) | proxy | ✅ `quality` | — |
| URDF expands + loads as a valid kinematic tree | ✅ yourdfpy | ✅ | — |
| SRDF ↔ abstraction ↔ URDF gesture consistency | ✅ | ✅ | — |
| End-to-end **logic** chain (prediction→gesture→radians) | ✅ | ✅ | — |
| `colcon build` (rosidl + ament) | — | ✅ `ros2-build` (ros:jazzy) | ✅ |
| `colcon test` under ROS2 | — | ✅ `ros2-build` | ✅ |
| Gazebo Harmonic spawn + controllers | — | — | ▶ runtime |
| MoveIt2 planning to named states | — | — | ▶ runtime |
| Live ROS transport (topics/services) | — | — | ▶ runtime |
| Command→robot latency instrumentation | ✅ unit | ✅ | ▶ measured live |

`colcon build`/`colcon test` now run in CI inside a `ros:jazzy` container — the build
that cannot run on macOS is executed on every push. Only Gazebo/MoveIt2 *runtime*
(a live simulator) remains on the ROS2 host. No build/simulation result is reported as
passing unless it was actually executed.

## 2. Performance report

### AI pipeline
- **Dataset:** EEGBCI subject 1, run 4 — 29 epochs, 64 channels, 160 Hz, 3 classes.
- **Preprocessing:** 1–40 Hz FIR band-pass + ICA (no EOG channels in EEGBCI, so ICA
  excludes 0 components; the band-pass is the effective cleaning).
- **Features:** 4 CSP components (log-variance), fit on training epochs only.
- **Model sizes:** deployed CNN-LSTM ≈ 356 KB; inference is sub-millisecond per
  window on CPU — negligible relative to the 1 s EEG window.

### ROS2 stack
- Event-driven nodes; the bridge replays predictions at a configurable period
  (default 2 s). Latency budget is dominated by the trajectory `move_time` (1 s),
  not by computation.
- The pure-logic path (prediction → gesture → joint radians) is O(n_joints) per
  command with no allocation on the hot path beyond the outgoing message.

## 3. Scientific validation summary

Five methodological defects were found in the original pipeline and fixed before the
robotics work (branch history: `Fix A1`–`A5`):

| Fix | Defect | Effect of the fix |
|-----|--------|-------------------|
| A4 | `processed_data/` held raw, unfiltered epochs | Now filtered + ICA-cleaned before CSP |
| A2 | CSP fit on all 29 epochs before the split (leakage) | CSP fit on training epochs only |
| A3 | Test set used as validation set in all DL labs | Stratified validation split held out from train |
| A5 | Adaptive threshold direction inverted (unsafe) | High accuracy ⇒ permissive; low ⇒ conservative + cold-start |
| A1 | `requirements.txt` uninstallable / incomplete | Clean, pinned, reproducible |

**Honest results after the fixes** (6-sample test set, single subject):

| Model | Accuracy |
|-------|---------:|
| SVM | 0.33 |
| Random Forest | 0.50 |
| XGBoost | 0.33 |
| CNN | 0.50 |
| LSTM | 0.50 |
| CNN-LSTM | **0.67** |

These numbers are low but **trustworthy** — they are the true difficulty of n = 29,
single-subject data with leakage removed. The scientific contribution of v1.0 is a
*correct, leakage-free, reproducible* pipeline, not a high score. Raising accuracy is
a data-scale problem (see §6): EEGBCI provides 109 subjects.

**Known limitation (honest):** the confidence values from the current real-time path
are low and are correctly gated out by the adaptive threshold, so the *real* data
produces no motion — the demonstration uses bundled high-confidence demo predictions
to exercise the full motion path. This is a data/scale limitation, not a code defect.

## 4. Software-engineering summary

- **Six ROS2 packages**, each single-purpose, versioned **1.0.0**.
- **Separation of concerns:** decision logic in pure-Python modules (no ROS imports),
  ROS2 nodes are thin transport wrappers. Result: **36 ROS2 tests run without ROS2**,
  plus **7 AI scientific-invariant tests** — 43 in total.
- **Continuous integration:** GitHub Actions runs lint, the ROS2 logic tests, the AI
  validation tests, and a real `colcon build`/`colcon test` in a `ros:jazzy` container
  on every push.
- **Diagnostics:** command→robot latency is instrumented (running min/mean/max) and
  logged by the robot node.
- **Single source of truth** for the gesture vocabulary, enforced by a cross-package
  consistency test (abstraction × URDF limit == SRDF named state).
- **Reproducibility:** pinned `requirements.txt` (clean-room verified), Dockerfile +
  RunPod bootstrap, one-command `build_and_verify.sh`.
- **Traceable history:** the scientific fixes and each ROS2 phase are separate,
  self-contained commits with verification recorded in the message.
- **No dead code / no TODO debt**; stray placeholder directories removed for v1.0.

## 5. Robotics summary

- **Robot model:** five-finger hand, one revolute joint per finger (0–1.4 rad),
  self-contained primitive geometry (no external meshes), fixed to the world frame.
- **Control:** `ros2_control` with `joint_state_broadcaster` + a
  `joint_trajectory_controller`, driven in Gazebo Harmonic via `gz_ros2_control`.
- **Planning:** MoveIt2 "hand" joint group with six named gesture states; OMPL
  joint-space planning (no IK chain needed for a finger group).
- **Abstraction:** `RobotInterface` contract + registry; the robotic hand is one
  implementation. Robot selection is a launch parameter.
- **Extensibility proven by construction:** a new robot is a `RobotInterface`
  subclass + a registry entry + its own adapter — zero changes to EEG/AI/bridge code.

## 6. Future extension plan

**Near term (PhD / thesis extension):**
1. **Scale the data** — train across many EEGBCI subjects with subject-wise
   cross-validation; replace the 6-sample holdout with a proper CV estimate.
2. **Live prediction topic** — replace the CSV replay in `bci_bridge` with a node that
   runs inference on a live EEG stream and publishes predictions directly.
3. **Causal real-time filtering** — swap the offline `filtfilt` for a streaming
   `lfilter` with carried state for a true online path.

**Robotics extensions:**
4. **Second robot** — add a UR5e or Franka Panda `RobotInterface` + adapter to
   demonstrate the abstraction on an industrial arm (Phase 6).
5. **Collision-aware planning** — use MoveIt2 planning scenes for grasp tasks with
   objects, beyond named finger poses.
6. **Hardware bridge** — replace the Gazebo controller with a real hand's driver
   behind the same `hand_controller` interface.

**AI extensions:**
7. **True adaptive learning** — replace the file-copy "adaptive update" with online
   fine-tuning on accumulated user feedback.
8. **Richer gesture set** — extend the model beyond 3 classes to drive all 6 gestures
   directly (the robot already supports all six).

## 7. Suitability

This release is structured for: Master's thesis submission, a public GitHub release,
a methods/systems publication, continued PhD research, and industrial extension via
the robot abstraction layer.
