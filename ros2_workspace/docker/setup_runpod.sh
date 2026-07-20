#!/usr/bin/env bash
#
# Bootstrap a bare Ubuntu 24.04 (Noble) RunPod pod with the full ROS2 Jazzy
# robot stack used by the Hybrid Adaptive BCI project. Use this when the pod
# starts from a stock Ubuntu/CUDA image rather than the provided Dockerfile.
#
# Usage (on the pod):
#   bash ros2_workspace/docker/setup_runpod.sh
#
set -euo pipefail

if [ "$(. /etc/os-release && echo "$VERSION_ID")" != "24.04" ]; then
  echo "WARNING: ROS2 Jazzy targets Ubuntu 24.04; detected a different release." >&2
fi

export DEBIAN_FRONTEND=noninteractive

echo "==> Enabling universe and adding the ROS2 apt repository"
apt-get update
apt-get install -y software-properties-common curl gnupg lsb-release
add-apt-repository -y universe

curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
  -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo "$UBUNTU_CODENAME") main" \
  > /etc/apt/sources.list.d/ros2.list

echo "==> Installing ROS2 Jazzy + Gazebo Harmonic + MoveIt2 + control stack"
apt-get update
apt-get install -y \
  ros-jazzy-ros-base \
  ros-jazzy-ros-gz \
  ros-jazzy-moveit \
  ros-jazzy-ros2-control \
  ros-jazzy-ros2-controllers \
  ros-jazzy-gz-ros2-control \
  ros-jazzy-xacro \
  ros-jazzy-joint-state-publisher \
  ros-jazzy-robot-state-publisher \
  python3-colcon-common-extensions \
  python3-rosdep \
  build-essential

echo "==> Initialising rosdep"
rosdep init 2>/dev/null || true
rosdep update

echo "==> Done. Next steps:"
echo "    source /opt/ros/jazzy/setup.bash"
echo "    cd ros2_workspace && bash docker/build_and_verify.sh"
