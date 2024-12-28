# robosys2024-assignment2
[![test](https://github.com/Hanb12-JO/robosys2024-assignment2/actions/workflows/test.yml/badge.svg)](https://github.com/Hanb12-JO/robosys2024-assignment2/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
## Demonstration
![demo](https://github.com/user-attachments/assets/e783f2af-7583-4594-9ae2-1a2a0af928d3)

## Overview

## Features

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
