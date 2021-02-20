#!/bin/bash



###export MQTTH="arena-dev1.conix.io"
export MQTTH="arena.andrew.cmu.edu"
export REALM="realm"
export SCENE="headsup-dev-17"



echo "MQTT server is $MQTTH"
echo "MQTT realm is $REALM"
echo "ARENA scene is $SCENE"



python3 headsup-server.py

