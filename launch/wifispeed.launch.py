# SPDX-FileCopyrightText: 2024 Abdelrahman Alhanbali <abdelrahman.alhanbali@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    wifispeed_talker = launch_ros.actions.Node(
            package = 'robosys2024_assignment2',
            executable = 'wifispeed_talker',
            )

    wifispeed_listner = launch_ros.actions.Node(
            package = 'robosys2024_assignment2',
            executable = 'wifispeed_listner',
            output = 'screen'
            )

    return launch.LaunchDescription([wifispeed_talker, wifispeed_listner])
