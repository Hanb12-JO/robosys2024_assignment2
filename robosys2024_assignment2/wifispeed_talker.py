# SPDX-FileCopyrightText: 2024 Abdelrahman Alhanbali <abdelrahman.alhanbali@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import speedtest
import math

# バイトからMbpsへの変換関数
def bytes_to_mb(size_bytes):
    i = int(math.floor(math.log(size_bytes, 1024)))  # size_bytesを1024で対数をとる。KB → MB → GB
    power = math.pow(1024, i)  # pow(4,3)で4の3乗
    size = round(size_bytes / power, 2)  # 小数点以下を2桁に丸める。
    return f"{size} Mbps"

class WifiSpeedPublisher(Node):
    def __init__(self):
        super().__init__('WifiSpeedSubscriber')
        self.pub = self.create_publisher(String, 'wifispeed', 10)
        self.wifi = speedtest.Speedtest()
        self.create_timer(1.0, self.cb)

    def cb(self):
        msg = String()
        msg.data = "Getting download speed..."
        download_speed = self.wifi.download()
        self.pub.publish(msg)

        msg.data = "Getting upload speed..."
        upload_speed = self.wifi.upload()
        self.pub.publish(msg)

            ### Mbpsに変換 ###
        download_speed_mbps = bytes_to_mb(download_speed)
        upload_speed_mbps = bytes_to_mb(upload_speed)

        msg.data = f"Download: {download_speed_mbps}, Upload: {upload_speed_mbps}"
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = WifiSpeedPublisher()
    rclpy.spin(node)

