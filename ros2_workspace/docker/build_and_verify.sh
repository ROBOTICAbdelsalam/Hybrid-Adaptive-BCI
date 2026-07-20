#!/usr/bin/env bash
#
# Build the BCI ROS2 workspace and run headless verification. Safe to run
# repeatedly. Executes the "build, run, verify" loop the project workflow
# requires. Run from anywhere; it locates the workspace root itself.
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WS_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

echo "==> Workspace: ${WS_ROOT}"
# shellcheck disable=SC1091
source /opt/ros/jazzy/setup.bash

cd "${WS_ROOT}"

echo "==> colcon build"
colcon build --symlink-install

# shellcheck disable=SC1091
source "${WS_ROOT}/install/setup.bash"

echo "==> Verifying generated interfaces are available"
FAILED=0
for iface in \
  "bci_interfaces/msg/BCICommand" \
  "bci_interfaces/msg/RobotState" \
  "bci_interfaces/srv/ExecuteGesture"; do
  if ros2 interface show "${iface}" >/dev/null 2>&1; then
    echo "    OK  ${iface}"
  else
    echo "    MISSING  ${iface}" >&2
    FAILED=1
  fi
done

if [ "${FAILED}" -ne 0 ]; then
  echo "==> Verification FAILED" >&2
  exit 1
fi

echo "==> Phase 1 verification passed: workspace builds and interfaces resolve."
