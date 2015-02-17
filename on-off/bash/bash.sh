#!/bin/bash

sudo echo $1 > /sys/class/gpio/export
cd /sys/class/gpio/gpio$1
echo out > direction
echo 1 > value
while true
do
	sleep 2
	echo 1 > value
	sleep 2
	echo 0 > value
done
