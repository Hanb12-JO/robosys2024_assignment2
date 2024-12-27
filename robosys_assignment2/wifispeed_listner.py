from rclpy.node import Node
from std_msgs.msg import String
import speedtest
import math

rclpy.init()
node = Node("wifispeed_sub")

def cb(msg):
    global node
    node.get_logger().info(f"Published: {msg.data}")

def main():
    sub = node.create_subscription(String, "wifispeed", cb, 10)
    rclpy.spin(node)
