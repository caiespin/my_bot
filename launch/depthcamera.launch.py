import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='realsense2_camera',
            executable='realsense2_camera_node',
            output='screen',
            # If you want a single 'camera' prefix, set only one of these:
            namespace='camera',  # <--- your namespace
            # camera_name='camera' can also be used, but might cause double '/camera/camera'

            parameters=[{
                'enable_depth': True,
                'enable_color': True,
                'enable_infra1': True,
                'enable_infra2': True,
                'align_depth': True,

                # ---- CRITICAL for the /points topic ----
                'filters': ['pointcloud'],     # Must explicitly load 'pointcloud'
                'pointcloud.enable': True,     # or 'enable_pointcloud': True
                # ----------------------------------------

                # Optionally allow uncolored points
                'allow_no_texture_points': True,

                # Set your desired FPS/resolution
                'depth_module.profile': '640x480x15',
                'rgb_camera.profile': '640x480x15',
                'infra1_module.profile': '640x480x15',
                'infra2_module.profile': '640x480x15',

                # TF frames
                'base_frame_id': 'camera_link',
                'depth_frame_id': 'camera_depth_frame',
                'color_frame_id': 'camera_color_frame',
                'infra1_frame_id': 'camera_infra1_frame',
                'infra2_frame_id': 'camera_infra2_frame',
                'depth_optical_frame_id': 'camera_depth_optical_frame',
                'pointcloud_frame_id': 'camera_depth_optical_frame',

                'tf_publish_rate': 30.0,
            }]
        )
    ])
