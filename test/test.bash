#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
ros2 run robosys_assignment2 wifispeed | tee - /tmp/robosys_assignment2	.log
