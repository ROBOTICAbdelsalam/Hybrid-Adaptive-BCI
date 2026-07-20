"""Robot-independent abstraction layer for the Hybrid Adaptive BCI.

The pure-Python core (gesture_library, robot_interface, robotic_hand_interface,
robot_registry) has no ROS2 dependency and is unit-tested directly. The ROS2
node (robot_node) is a thin transport wrapper around that core.
"""
