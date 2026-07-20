"""AI -> ROS2 bridge node.

Turns the EEG/AI pipeline's predictions into robot-independent BCICommand
messages on ``/bci/command``. It reads the CSV the pipeline already writes
(Lab 14.4) and the adaptive confidence gate (Lab 13.2), so no AI code is
modified. Predictions are replayed at a fixed rate to emulate the live stream;
a later phase can swap the CSV source for a live prediction topic without
touching the abstraction or robot layers.

Thin transport wrapper: all mapping/gating logic is in the tested pure-Python
prediction_source module.
"""

from __future__ import annotations

import rclpy
from rclpy.node import Node

from bci_interfaces.msg import BCICommand

from . import prediction_source as ps


class BridgeNode(Node):
    def __init__(self) -> None:
        super().__init__("bci_bridge_node")

        self.declare_parameter("predictions_csv", "")
        self.declare_parameter("threshold_csv", "")
        self.declare_parameter("publish_period_sec", 1.0)
        self.declare_parameter("loop", True)

        self._predictions_csv = self.get_parameter("predictions_csv").value
        self._threshold_csv = self.get_parameter("threshold_csv").value
        self._loop = bool(self.get_parameter("loop").value)
        period = float(self.get_parameter("publish_period_sec").value)

        self._pub = self.create_publisher(BCICommand, "/bci/command", 10)

        self._threshold = (
            ps.load_threshold(self._threshold_csv)
            if self._threshold_csv else ps.DEFAULT_THRESHOLD
        )
        self._predictions = (
            ps.read_predictions(self._predictions_csv)
            if self._predictions_csv else []
        )
        self._index = 0

        self.get_logger().info(
            f"Bridge started: {len(self._predictions)} predictions, "
            f"threshold={self._threshold:.2f}, period={period:.2f}s"
        )

        if self._predictions:
            self.create_timer(period, self._tick)
        else:
            self.get_logger().warn(
                "No predictions loaded; set the 'predictions_csv' parameter.")

    def _tick(self) -> None:
        if self._index >= len(self._predictions):
            if not self._loop:
                self.get_logger().info("Prediction stream finished.")
                return
            self._index = 0

        pred = self._predictions[self._index]
        self._index += 1

        gesture, reason = ps.to_gesture(pred, self._threshold)
        if gesture is None:
            self.get_logger().info(f"skip: {reason}")
            return

        msg = BCICommand()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.gesture = gesture
        msg.confidence = float(pred.confidence)
        msg.source = "eeg_ai_pipeline"
        self._pub.publish(msg)
        self.get_logger().info(
            f"publish gesture={gesture} conf={pred.confidence:.2f}")


def main(args=None) -> None:
    rclpy.init(args=args)
    node = BridgeNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
