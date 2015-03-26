#!/bin/bash

#This is a script to restart siege.

# Kill existing load
date > /appd/siegelog
echo "Killing Load Script" >> /appd/siegelog
echo `ps -ef | grep siege | grep -v grep | awk '{print $2}'`
kill -9 `ps -ef | grep siege | grep -v grep | awk '{print $2}'`

# Start Load
echo "Starting Load Script" >> /appd/siegelog
nohup siege -d 1 -f /appd/siege.txt &
