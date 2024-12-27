#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 60 ros2 run robosys_assignment2 wifispeed | tee - /tmp/robosys_assignment2.log
sleep 2


cat /tmp/robosys_assignment2.log | grep 'Published'
#grep 'wifispeed' #&& 'Getting download speed...'
#grep 'Publish'
#grep 'wifispeed' && 'Published'


