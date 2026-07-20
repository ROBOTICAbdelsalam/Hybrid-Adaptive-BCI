"""Launch the BCI robotic hand in Gazebo Harmonic with ros2_control.

Brings up:
  * Gazebo Harmonic (empty world),
  * robot_state_publisher with the xacro-expanded hand,
  * the hand spawned into the sim,
  * joint_state_broadcaster and hand_controller (joint_trajectory_controller).

Run on a ROS2 Jazzy host:
    ros2 launch bci_hand_description gazebo.launch.py
"""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    RegisterEventHandler,
)
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    pkg = get_package_share_directory("bci_hand_description")
    xacro_file = os.path.join(pkg, "urdf", "bci_hand.urdf.xacro")
    controllers_yaml = os.path.join(pkg, "config", "hand_controllers.yaml")

    # Expand xacro at launch time, injecting the absolute controllers path.
    robot_description = {
        "robot_description": Command([
            "xacro ", xacro_file,
            " controllers_config:=", controllers_yaml,
        ])
    }

    gui = LaunchConfiguration("gui")

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare("ros_gz_sim"),
                "launch", "gz_sim.launch.py",
            ])
        ]),
        launch_arguments={"gz_args": "-r -v 3 empty.sdf"}.items(),
    )

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[robot_description, {"use_sim_time": True}],
    )

    spawn_entity = Node(
        package="ros_gz_sim",
        executable="create",
        output="screen",
        arguments=["-topic", "robot_description", "-name", "bci_hand", "-z", "0.0"],
    )

    clock_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=["/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock"],
        output="screen",
    )

    load_jsb = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster"],
        output="screen",
    )

    load_hand = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["hand_controller"],
        output="screen",
    )

    # Start controllers only after the hand has spawned.
    controllers_after_spawn = RegisterEventHandler(
        OnProcessExit(target_action=spawn_entity, on_exit=[load_jsb])
    )
    hand_after_jsb = RegisterEventHandler(
        OnProcessExit(target_action=load_jsb, on_exit=[load_hand])
    )

    return LaunchDescription([
        DeclareLaunchArgument("gui", default_value="true",
                              description="Start the Gazebo GUI"),
        gz_sim,
        robot_state_publisher,
        clock_bridge,
        spawn_entity,
        controllers_after_spawn,
        hand_after_jsb,
    ])
