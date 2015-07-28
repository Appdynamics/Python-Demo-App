#!/bin/bash

# This is a script to start Python on Docker

# Set variables
CONTR_HOST=
CONTR_PORT=8090
SIEGE_URL=http://www.appdynamics.com
SSL=off
ACCOUNT_NAME=
ACCESS_KEY=
APP_NAME=
TIER_NAME=
NODE_NAME=

echo "${CONTR_HOST} is the controller name and ${CONTR_PORT} is the controller port"

# Pull images
docker pull appdynamics/python-base:latest
docker pull appdynamics/python-mysql:latest
docker pull appdynamics/python-postgres:latest
docker pull appdynamics/python-app:latest
docker pull appdynamics/python-siege:latest

# Start containers 
docker run -d --name python_mysql -p 3306:3306 appdynamics/python-mysql:latest
docker run -d --name python_postgresql -p 5432:5432 appdynamics/python-postgresql:latest
sleep 10
docker run -d --name python_app -p 9000:9000 \
	-e ACCOUNT_NAME=${ACCOUNT_NAME} -e ACCESS_KEY=${ACCESS_KEY} -e SSL=${SSL}\
	-e CONTROLLER=${CONTR_HOST} -e APPD_PORT=${CONTR_PORT} \
	-e APP_NAME=${APP_NAME} -e TIER_NAME=${TIER_NAME} -e NODE_NAME=${NODE_NAME} \
	--link python_mysql:python_mysql --link python_postgresql:python_postgresql appdynamics/python-app:latest
docker run -d --name python_siege -e BUNDY_TIER=${SIEGE_URL} --link python_app:python_app appdynamics/python-siege:latest

exit 0
