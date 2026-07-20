# Reproducible ROS2 Jazzy environment for the Hybrid Adaptive BCI robot stack.
#
# Target: RunPod (or any Ubuntu 24.04 host / amd64 or arm64).
# Pairs ROS2 Jazzy with Gazebo Harmonic and MoveIt2, which is the officially
# supported combination for Jazzy.
#
# Build:  docker build -t bci-ros2:jazzy -f docker/Dockerfile .
# Run:    docker run -it --rm bci-ros2:jazzy
# (headless verification works out of the box; GUI needs X11 forwarding)

FROM ros:jazzy-ros-base

ENV DEBIAN_FRONTEND=noninteractive
ENV ROS_DISTRO=jazzy

# ---------------------------------------------------------------------------
# Simulation, motion planning and control stack
# ---------------------------------------------------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-jazzy-ros-gz \
    ros-jazzy-moveit \
    ros-jazzy-ros2-control \
    ros-jazzy-ros2-controllers \
    ros-jazzy-gz-ros2-control \
    ros-jazzy-xacro \
    ros-jazzy-joint-state-publisher \
    ros-jazzy-robot-state-publisher \
    python3-colcon-common-extensions \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# ---------------------------------------------------------------------------
# Workspace
# ---------------------------------------------------------------------------
WORKDIR /bci_ws
COPY . /bci_ws/

# Resolve declared package dependencies, then build.
RUN . /opt/ros/jazzy/setup.sh \
    && apt-get update \
    && rosdep update \
    && rosdep install --from-paths src --ignore-src -r -y || true \
    && rm -rf /var/lib/apt/lists/*

RUN . /opt/ros/jazzy/setup.sh \
    && colcon build --symlink-install

# Source ROS2 and the workspace overlay on every interactive shell.
RUN echo "source /opt/ros/jazzy/setup.bash" >> /root/.bashrc \
    && echo "source /bci_ws/install/setup.bash" >> /root/.bashrc

CMD ["bash"]
