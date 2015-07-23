#!/bin/bash

# This is a starup script for the siege container in Python Demo app

# Define siege URL
source /appd/env.sh
sed -i "/^EXTERNAL/c\EXTERNAL=${BUNDY_TIER}" /appd/siege.txt

# Stop siege load 
echo `ps -ef | grep -i siege | grep -v grep | awk '{print $2}'`
kill -9 `ps -ef | grep -i siege | grep -v grep | awk '{print $2}'`

# Start services
counter=1000
if [ -z $counter ]; then
  counter=1
fi;

echo "Run siege $counter iteration(s)";

x=1;

while [ $x -le $counter ]
do
  echo "Iteration $x starting..."
  siege -d5 -t24H -c8 -f /appd/siege.txt > /appd/nohup-siege.out
  x=$(( $x + 1 ));
  echo "Iteration $x complete. Rest 15 seconds and reiterate."
  sleep 15;
done;
echo "Completed $counter iteration(s)"
