# robosys2024-assignment2
[![test](https://github.com/Hanb12-JO/robosys2024-assignment2/actions/workflows/test.yml/badge.svg)](https://github.com/Hanb12-JO/robosys2024-assignment2/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
## Demonstration
![demo](https://github.com/user-attachments/assets/e783f2af-7583-4594-9ae2-1a2a0af928d3)

## Overview
This package uses ROS2 to measure and publish internet download and upload speeds. The data is published to a topic and received by a subscriber node, which logs the results to the display.
## Features
* Can measure the download and upload speeds of internet.
* Publishe the measurement results via a ROS2 topic, which the subscriber node receives and logs.
## Require environment
  * ubuntu 22.04 and later

## Setup
  This ROS2 package use speedtest library on python.Please copy the below command to install speedtest environment.
```bash
pip install speedtest-cli
```

## How to use this node
#### 1. Add this project in ROS2 workspace
```bash
cd ~/ros2_ws/src
git clone https://github.com/Hanb12-JO/robosys2024-assignment2.git
```
#### 2. Build and source
```bash
cd ~/ros2_ws/
colcon build
source ~/.bashrc  #source install/setup.bash also availabal
```
#### 3. Run
* Run the publisher in **Desktop1**.
```bash
ros2 run robosys_assignment2 wifispeed_talker
```
* Run subscriber in **Desktop2**.
```bash
ros2 run robosys_assignment2 wifispeed_listner
```
#### 4. Launch
If you want to launch multiple nodes at the same time, please use the following launch command: 
```bash
ros2 launch robosys_assignment2 wifispeed.launch.py
```
*Note: It may take a long time for the nodes to appear after launching.*
#### 5.Output
The output will be the same as the demonstration at the top of the page.

## Troubleshooting
During the execution of the `wifispeed_talker` node, you may encounter the following error:
```
speedtest.ConfigRetrievalError: HTTP Error 403: Forbidden
```
This error can occur due to temporary network issues or when the external `Speedtest` API is temporarily unavailable. If this happens, please wait for a few minutes and try running the program again.  

If the issue persists, check the following
1. Ensure that your internet connection is stable and active.
2. Verify that the Speedtest CLI is updated to the latest version.
3. Confirm that network restrictions (proxies or firewalls) are not causing the problem.  

## References  
* [Python Internet Speed Test Tutorial 2022 (Fast & Easy)](https://www.youtube.com/watch?v=QkMyJatG1Lo)

© 2024 Abdelrahman Alhanbali. All Rights Reserved.
