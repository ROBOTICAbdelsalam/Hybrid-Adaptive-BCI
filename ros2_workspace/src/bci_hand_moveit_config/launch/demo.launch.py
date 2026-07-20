"""MoveIt2 demo for the BCI hand: move_group + RViz motion-planning display.

Use this to verify planning to the six named gesture states interactively:

    ros2 launch bci_hand_moveit_config demo.launch.py

In RViz, set the "hand" planning group and plan/execute to each named state
(rest, open_hand, close_hand, pinch_grip, power_grip, point).
"""

from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch


def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder("bci_hand", package_name="bci_hand_moveit_config")
        .to_moveit_configs()
    )
    return generate_demo_launch(moveit_config)
