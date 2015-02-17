#!/bin/bash

sudo echo $1 > /sys/class/gpio/export
cd /sys/class/gpio/gpio$1
echo out > direction
echo 1 > value
while true
do
	echo 1 > value
	echo 0 > value
done
