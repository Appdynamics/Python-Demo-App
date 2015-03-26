#!/bin/bash

# This is a starup script for the siege container in Python Demo app

# Define siege URL
source /appd/env.sh
sed -i "/^EXTERNAL/c\EXTERNAL=${BUNDY_TIER}" /appd/siege.txt

# Start services
cron -f &
source /appd/restartload.sh

exit 0
