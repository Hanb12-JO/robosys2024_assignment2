# robosys2024_assignment2
[![test](https://github.com/Hanb12-JO/robosys2024_assignment2/actions/workflows/test.yml/badge.svg)](https://github.com/Hanb12-JO/robosys2024_assignment2/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
## Demonstration
![demo](https://github.com/user-attachments/assets/e6ca0cc3-0864-43e4-b89c-1f630a33a573)

## Overview
This package uses ROS2 to measure and publish internet download and upload speeds. The data is published to a topic and received by a subscriber node, which logs the results to the display.
## Features
* Can measure the download and upload speeds of the internet.
* The measurement results are published via a ROS2 topic, which the subscriber node receives and logs.
## Require environment
* Ubuntu 22.04 and later

## Setup
This ROS2 package uses speedtest library in Python. Please copy the below command to install the speedtest environment.
```bash
pip install speedtest-cli
```

## How to use this node
#### 1. Add this project in ROS2 workspace
```bash
cd ~/ros2_ws/src
git clone https://github.com/Hanb12-JO/robosys2024-assignment2.git
```
*Note: Replace *`ros2_ws`* with the name of your ROS2 workspace directory if it is different.*
#### 2. Run
* Run the publisher in **Desktop1**.
```bash
ros2 run robosys_assignment2 wifispeed_talker
```
* Run subscriber in **Desktop2**.
```bash
ros2 run robosys_assignment2 wifispeed_listner
```
#### 3. Launch
If you want to launch multiple nodes at the same time, please use the following launch command: 
```bash
ros2 launch robosys_assignment2 wifispeed.launch.py
```
*Note: The nodes may take a long time to appear after launching.*
#### 4. Output
The output will be the same as the demonstration at the top of the page.
## Node
#### 1. WifiSpeedPublisher
The `WifiSpeedPublisher` is a ROS2 node that measures internet download and upload speeds using the `Speedtest` library and publishes results on the `wifispeed` topic in Mbps. It tests internet speed regularly and sends the data to the topic.  
#### 2. WifiSpeedSubscriber
The `WifiSpeedSubscriber` node subscribes to the `wifispeed` topic, where it receives internet download and upload speed data published by the `WifiSpeedPublisher` node. Upon receiving the data, it logs the results, including both download and upload speeds.
```bash
[wifispeed_listner-2] [INFO] [1735721805.214572734] [wifispeed_sub]: Getting download speed...
[wifispeed_listner-2] [INFO] [1735721815.372325707] [wifispeed_sub]: Getting upload speed...
[wifispeed_listner-2] [INFO] [1735721815.372753008] [wifispeed_sub]: Download: 47.64 Mbps, Upload: 88.35 Mbps
```
## Topic
The `wifispeed` topic is a communication channel between the `WifiSpeedPublisher` and `WifiSpeedSubscriber` nodes. 

## Troubleshooting
During the execution of the `wifispeed_talker` node, you may encounter the following error:
```
speedtest.ConfigRetrievalError: HTTP Error 403: Forbidden
```
This error can occur due to temporary network issues or when the external `Speedtest` API is temporarily unavailable. If this happens, please wait a few minutes and try running the program again.  

If the issue persists, check the following: 
1. Ensure that your internet connection is stable and active.
2. Verify that the Speedtest CLI is updated to the latest version.
3. Confirm that network restrictions (proxies or firewalls) are not causing the problem.  

## References  
* [Python Internet Speed Test Tutorial 2022 (Fast & Easy)](https://www.youtube.com/watch?v=QkMyJatG1Lo)

© 2024 Abdelrahman Alhanbali. All Rights Reserved.
