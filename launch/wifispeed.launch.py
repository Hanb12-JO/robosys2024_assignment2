import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    wifispeed_talker = launch_ros.actions.Node(
            package = 'robosys_assignment2',
            executable = 'wifispeed_talker',
            )

    wifispeed_listner = launch_ros.actions.Node(
            package = 'robosys_assignment2',
            executable = 'wifispeed_listner',
            output = 'screen'
            )

    return launch.LaunchDescription([wifispeed_talker, wifispeed_listner])
