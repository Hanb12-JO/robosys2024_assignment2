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
  This ROS2 package use speedtest library on python.Please copy the bellow command to install speedtest environment.
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
cd ..
colcon build
source ~/.bashrc
```
#### 3. Launch
```bash
ros2 launch robosys_assignment2 wifispeed.launch.py
```
