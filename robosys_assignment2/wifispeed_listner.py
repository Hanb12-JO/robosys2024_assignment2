import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class WifiSpeedSubscriber(Node):
    def __init__(self):
        super().__init__("wifispeed_sub")
        self.create_subscription(String, "wifispeed", self.cb, 10)

    def cb(self, msg):
        self.get_logger().info(f"{msg.data}")

def main():
    rclpy.init()
    node = WifiSpeedSubscriber()
    rclpy.spin(node)

