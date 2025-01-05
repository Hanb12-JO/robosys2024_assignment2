# SPDX-FileCopyrightText: 2024 Abdelrahman Alhanbali <abdelrahman.alhanbali@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class WifiSpeedSubscriber(Node):
    def __init__(self):
        super().__init__("WifiSpeedSubscriber")
        self.create_subscription(String, "wifispeed", self.cb, 10)

    def cb(self, msg):
        self.get_logger().info(f"{msg.data}")

def main():
    rclpy.init()
    node = WifiSpeedSubscriber()
    rclpy.spin(node)

