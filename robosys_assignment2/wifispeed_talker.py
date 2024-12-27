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
        super().__init__('wifi_speed_publisher')
        self.pub = self.create_publisher(String, 'wifispeed', 10)
        self.wifi = speedtest.Speedtest()
        self.create_timer(5.0, self.cb)  # 5秒ごとに速度を測定して送信

    def cb(self):
        # Wi-Fi速度を計測
        download_speed = self.wifi.download()
        upload_speed = self.wifi.upload()

        # Mbpsに変換
        download_speed_mbps = bytes_to_mbps(download_speed)
        upload_speed_mbps = bytes_to_mbps(upload_speed)

        # メッセージを作成してパブリッシュ
        msg = String()
        msg.data = f"Download: {download_speed_mbps} Mbps, Upload: {upload_speed_mbps} Mbps"
        self.pub.publish(msg)

        # ログに出力
        #self.get_logger().info(f"Published: {message.data}")

def main():
    rclpy.init()
    node = WifiSpeedPublisher()
    rclpy.spin(node)
