"""Hand-specific adapter: normalised joint targets -> JointTrajectory.

The robot abstraction layer is robot-independent and emits normalised finger
flexion in [0, 1] on ``/bci/joint_targets``. This node is the hand-specific
glue that scales those to radians (via the URDF joint limit) and drives the
ros2_control ``hand_controller``. Keeping the scaling here - not in the
abstraction - is what lets an arm use a different adapter without changing any
upstream code.

The scaling is a pure function so it is unit-tested off-ROS.
"""

from __future__ import annotations

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration

from bci_robot_abstraction.robotic_hand_interface import FINGER_JOINTS

from .scaling import scale_to_radians


class HandTrajectoryAdapter(Node):
    def __init__(self) -> None:
        super().__init__("hand_trajectory_adapter")

        self.declare_parameter("max_flexion", 1.4)
        self.declare_parameter("move_time_sec", 1.0)
        self.declare_parameter(
            "controller_topic", "/hand_controller/joint_trajectory")

        self._max_flexion = float(self.get_parameter("max_flexion").value)
        self._move_time = float(self.get_parameter("move_time_sec").value)
        topic = self.get_parameter("controller_topic").value

        self._joint_names = list(FINGER_JOINTS)
        self._pub = self.create_publisher(JointTrajectory, topic, 10)
        self.create_subscription(
            Float64MultiArray, "/bci/joint_targets", self._on_targets, 10)

        self.get_logger().info(
            f"Hand adapter ready: max_flexion={self._max_flexion} rad, "
            f"-> {topic}")

    def _on_targets(self, msg: Float64MultiArray) -> None:
        if len(msg.data) != len(self._joint_names):
            self.get_logger().warn(
                f"expected {len(self._joint_names)} targets, "
                f"got {len(msg.data)}; ignoring")
            return

        positions = scale_to_radians(list(msg.data), self._max_flexion)

        traj = JointTrajectory()
        traj.joint_names = self._joint_names
        point = JointTrajectoryPoint()
        point.positions = positions
        point.time_from_start = Duration(
            sec=int(self._move_time),
            nanosec=int((self._move_time % 1.0) * 1e9))
        traj.points = [point]

        self._pub.publish(traj)
        self.get_logger().info(
            f"trajectory -> {[round(p, 2) for p in positions]} rad")


def main(args=None) -> None:
    rclpy.init(args=args)
    node = HandTrajectoryAdapter()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
