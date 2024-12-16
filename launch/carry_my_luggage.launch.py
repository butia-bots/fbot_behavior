from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory
from pathlib import Path

def generate_launch_description():
    # Get the package share directory
    package_share_dir = get_package_share_directory('fbot_behavior')
    config_file = str(Path(package_share_dir) / 'carry_my_luggage.config.yaml')

    # Return the launch description
    return LaunchDescription([
        IncludeLaunchDescription(
            PathJoinSubstitution([FindPackageShare('fbot_bringup'), 'full_bringup.launch.py']),
            launch_arguments=[('config_file_path', config_file)]
        )
    ])
