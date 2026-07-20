"""Start the MoveIt2 move_group for the BCI hand.

    ros2 launch bci_hand_moveit_config move_group.launch.py
"""

from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_move_group_launch


def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder("bci_hand", package_name="bci_hand_moveit_config")
        .to_moveit_configs()
    )
    return generate_move_group_launch(moveit_config)
