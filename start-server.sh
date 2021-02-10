#!/bin/bash

#export MQTTH="arena.andrew.cmu.edu"
export MQTTH="arena-dev1.conix.io"
export REALM="realm"
export SCENE="headsup-dev-17"

echo $MQTTH
echo $REALM
echo $SCENE

python3 headsup-server.py
