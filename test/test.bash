#!/bin/bash -xv
# SPDX-FileCopyrightText: 2024 Abdelrahman Alhanbali <abdelrahman.alhanbali@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 60 ros2 launch robosys2024_assignment2 wifispeed.launch.py | tee - /tmp/robosys2024_assignment2.log


cat /tmp/robosys2024_assignment2.log | 
grep 'Mbps'
