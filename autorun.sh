#!/bin/sh

DIR=$(dirname "$0")
if [ -f "/sys/devices/platform/avrctl/3g_power" ]
then
    logger "main board..."
    ifconfig eth0 192.168.0.200 netmask 255.255.255.0
    export DISPLAY=:0.0
    xhost +
    cd $DIR/busTest
    logger $DIR
    python bustest.py
else
    logger "seconardy board..."
    ifconfig eth0 192.168.0.201 netmask 255.255.255.0
    /ucast_tests/test_serial_port /dev/ttymxc4 115200 echo &
    export DISPLAY=:0.0
    xhost +
    cd $DIR/busTest
    logger $DIR
    python bustest_fuban.py
fi