import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        # LiDAR node
        Node(
            package='ldlidar_stl_ros2',
            executable='ldlidar_stl_ros2_node',
            name='LD06',
            output='screen',
            parameters=[{
                'port_name': '/dev/ttyLidar',
                'frame_id': 'laser_frame',
                'product_name': 'LDLiDAR_LD06',
                'topic_name': 'scan',
                'port_baudrate': 230400,
                'laser_scan_dir': True,
                'enable_angle_crop_func': False
            }]
        ),

        # Static Transform Publisher (adds the missing TF)
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='base_link_to_laser_tf',
            arguments=['0.067', '0', '0.1057', '0', '0', '0', 'base_link', 'laser_frame']
        )
    ])
