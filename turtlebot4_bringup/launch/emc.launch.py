#!/usr/bin/env python3
# Copyright 2021 Clearpath Robotics, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# @author Roni Kreinin (rkreinin@clearpathrobotics.com)


from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

from launch_ros.actions import Node

def generate_launch_description():

    pkg_turtlebot4_bringup = get_package_share_directory('turtlebot4_bringup')

    param_file_cmd = DeclareLaunchArgument(
        'param_file',
        default_value=PathJoinSubstitution(
            [pkg_turtlebot4_bringup, 'config', 'emc.yaml']),
        description='Turtlebot4 Robot param file'
    )

    turtlebot4_param_yaml_file = LaunchConfiguration('param_file')

    # Launch files
    turtlebot4_robot_launch_file = PathJoinSubstitution(
        [pkg_turtlebot4_bringup, 'launch', 'robot.launch.py'])

    standard_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([turtlebot4_robot_launch_file]),
        launch_arguments=[('model', 'standard'),
                          ('param_file', turtlebot4_param_yaml_file)])

    emc_tests = Node(
         package='turtlebot4_tests',
         executable='emc_tests',
         output='screen')

    ld = LaunchDescription()
    ld.add_action(param_file_cmd)
    ld.add_action(standard_launch)
    ld.add_action(emc_tests)
    return ld
