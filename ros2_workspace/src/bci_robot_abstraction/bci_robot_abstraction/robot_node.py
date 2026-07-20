"""ROS2 node wrapping a :class:`RobotInterface` implementation.

Robot-independence lives here: the ``robot_type`` parameter selects which
robot to instantiate from the registry, so the same node drives a robotic
hand today and an industrial arm tomorrow with no code change.

Responsibilities:
  * subscribe to ``/bci/command`` (BCICommand) from the AI bridge,
  * expose ``/bci/execute_gesture`` (ExecuteGesture) for direct clients,
  * publish ``/bci/robot_state`` (RobotState) feedback,
  * publish the planned joint targets on ``/bci/joint_targets`` for the
    simulation/controller layer (wired up in the Gazebo/MoveIt phases).

Thin by design: all decision logic is in the tested pure-Python core.
"""

from __future__ import annotations

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray

from bci_interfaces.msg import BCICommand, RobotState
from bci_interfaces.srv import ExecuteGesture

from .robot_registry import available_robots, create_robot
from .robotic_hand_interface import FINGER_JOINTS


class RobotNode(Node):
    def __init__(self) -> None:
        super().__init__("bci_robot_node")

        self.declare_parameter("robot_type", "robotic_hand")
        robot_type = self.get_parameter("robot_type").value

        try:
            self.robot = create_robot(robot_type)
        except KeyError as exc:
            self.get_logger().error(str(exc))
            raise

        self.get_logger().info(
            f"Robot node started for '{self.robot.name}' "
            f"(available: {available_robots()})"
        )

        self._state_pub = self.create_publisher(
            RobotState, "/bci/robot_state", 10)
        self._targets_pub = self.create_publisher(
            Float64MultiArray, "/bci/joint_targets", 10)

        self.create_subscription(
            BCICommand, "/bci/command", self._on_command, 10)
        self.create_service(
            ExecuteGesture, "/bci/execute_gesture", self._on_service)

    # -- command intake -----------------------------------------------------

    def _dispatch(self, gesture: int, confidence: float) -> tuple[bool, str]:
        """Run a gesture through the abstraction and publish the outcome."""
        result = self.robot.execute_gesture(gesture, confidence)

        state = RobotState()
        state.header.stamp = self.get_clock().now().to_msg()
        state.robot_id = self.robot.name
        state.current_gesture = gesture
        if result.accepted:
            state.status = RobotState.EXECUTING
            self._publish_targets(result.joint_targets)
        else:
            state.status = RobotState.REJECTED
        state.message = result.message
        self._state_pub.publish(state)

        self.get_logger().info(
            f"gesture={gesture} conf={confidence:.2f} -> "
            f"{'ACCEPT' if result.accepted else 'REJECT'}: {result.message}"
        )
        return result.accepted, result.message

    def _on_command(self, msg: BCICommand) -> None:
        self._dispatch(msg.gesture, msg.confidence)

    def _on_service(self, request, response):
        accepted, message = self._dispatch(request.gesture, request.confidence)
        response.accepted = accepted
        response.message = message
        return response

    # -- controller bridge --------------------------------------------------

    def _publish_targets(self, joint_targets: dict[str, float]) -> None:
        """Publish joint targets in a fixed joint order for the controllers."""
        if not joint_targets:
            return
        ordered = [joint_targets.get(j, 0.0) for j in FINGER_JOINTS]
        self._targets_pub.publish(Float64MultiArray(data=ordered))


def main(args=None) -> None:
    rclpy.init(args=args)
    node = RobotNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
