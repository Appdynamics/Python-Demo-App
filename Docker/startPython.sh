#!/bin/bash

# This is a script to start Python on Docker

# Set variables
CONTR_HOST=
CONTR_PORT=
SIEGE_URL=
echo "${CONTR_HOST} is the controller name and ${CONTR_PORT} is the controller port"

# Pull images
docker pull appdynamics/python-base:latest
docker pull appdynamics/python-mysql:latest
docker pull appdynamics/python-postgres:latest
docker pull appdynamics/python-app:latest
docker pull appdynamics/python-siege:latest

# Start containers 
docker run -d --name python_mysql -p 3306:3306 -v /etc/localtime:/etc/localtime:ro appdynamics/python-mysql:latest
docker run -d --name python_postgres -p 5432:5432 -v /etc/localtime:/etc/localtime:ro appdynamics/python-postgres:latest
sleep 10
docker run -d --name python_app -p 9000:9000 -e CONTROLLER=${CONTR_HOST} -e APPD_PORT=${CONTR_PORT} --link python_mysql:python_mysql --link python_postgres:python_postgres -v /etc/localtime:/etc/localtime:ro appdynamics/python-app:latest
docker run -d --name python_siege -e BUNDY_TIER=${SIEGE_URL} --link python_app:python_app -v /etc/localtime:/etc/localtime:ro appdynamics/python-siege:latest

exit 0
