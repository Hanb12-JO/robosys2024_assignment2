#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 60 ros2 launch robosys_assignment2 wifispeed.launch.py | tee - /tmp/robosys_assignment2.log


cat /tmp/robosys_assignment2.log | 
grep 'Mbps'
