"""Complete Hybrid Adaptive BCI system: EEG/AI predictions -> robotic hand.

Pipeline:
    EEG -> Preprocessing -> Features -> AI Model -> Prediction   (Labs 01-14)
        -> bridge_node  (/bci/command)
        -> robot_node   (abstraction, /bci/joint_targets + /bci/robot_state)
        -> hand_trajectory_adapter (/hand_controller/joint_trajectory)
        -> Gazebo Harmonic robotic hand

Predictions default to bundled demo data so the demo runs standalone; point
'predictions_csv' at realtime/results/realtime_predictions.csv to replay the
real Lab 14 output. No EEG/AI code is modified.

    ros2 launch bci_bringup bci_system.launch.py
"""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    bringup_share = get_package_share_directory("bci_bringup")
    demo_predictions = os.path.join(
        bringup_share, "config", "demo_predictions.csv")
    demo_threshold = os.path.join(
        bringup_share, "config", "demo_threshold.csv")

    gazebo_hand = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([
            FindPackageShare("bci_hand_description"),
            "launch", "gazebo.launch.py",
        ])),
    )

    robot_node = Node(
        package="bci_robot_abstraction",
        executable="robot_node",
        name="bci_robot_node",
        parameters=[{"robot_type": "robotic_hand"}],
        output="screen",
    )

    bridge_node = Node(
        package="bci_bridge",
        executable="bridge_node",
        name="bci_bridge_node",
        parameters=[{
            "predictions_csv": LaunchConfiguration("predictions_csv"),
            "threshold_csv": LaunchConfiguration("threshold_csv"),
            "publish_period_sec": LaunchConfiguration("publish_period_sec"),
            "loop": True,
        }],
        output="screen",
    )

    hand_adapter = Node(
        package="bci_bringup",
        executable="hand_trajectory_adapter",
        name="hand_trajectory_adapter",
        parameters=[{"max_flexion": 1.4, "move_time_sec": 1.0}],
        output="screen",
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            "predictions_csv", default_value=demo_predictions,
            description="CSV of (Prediction,Confidence); default is demo data"),
        DeclareLaunchArgument(
            "threshold_csv", default_value=demo_threshold,
            description="Adaptive threshold CSV (Lab 13.2 format)"),
        DeclareLaunchArgument(
            "publish_period_sec", default_value="2.0",
            description="Seconds between replayed predictions"),
        gazebo_hand,
        robot_node,
        bridge_node,
        hand_adapter,
    ])
