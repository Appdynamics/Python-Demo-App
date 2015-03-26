#!/bin/bash

# This is a starup script for the Python Demo app

# Set EC2 Region variable
source /appd/env.sh && sed -i "/^host/c\host = ${CONTROLLER}" /appd/Python-Demo-App/appdynamics.cfg
source /appd/env.sh && sed -i "/^port/c\port = ${APPD_PORT}" /appd/Python-Demo-App/appdynamics.cfg
#source /appdynamics/env.sh && sed -i "/^EXTERNAL/c\EXTERNAL=${BUNDY_TIER}" /appdynamics/Python-Demo-App/siege.txt
sed -i 's/localhost/python_mysql/g' /appd/Python-Demo-App/demo/config.py
sed -i 's/127.0.0.1/python_postgres/g' /appd/Python-Demo-App/demo/config.py
chown -R appdynamics.appdynamics /appd

# Setup virtualenv
#virtualenv /appdynamics/Python-Demo-App/env
#/appdynamics/Python-Demo-App/env/bin/pip install appdynamics
#/appdynamics/Python-Demo-App/env/bin/pip install --allow-external mysql-connector-python -r /appdynamics/Python-Demo-App/requirements.txt
#/appdynamics/Python-Demo-App/env/bin/pip install -r /appdynamics/Python-Demo-App/requirements.txt
su - appdynamics -c "virtualenv /appd/Python-Demo-App/env"
su - appdynamics -c "/appd/Python-Demo-App/env/bin/pip install --pre appdynamics"
su - appdynamics -c "/appd/Python-Demo-App/env/bin/pip install --allow-external mysql-connector-python -r /appd/Python-Demo-App/requirements.txt"
su - appdynamics -c "/appd/Python-Demo-App/env/bin/pip install -r /appd/Python-Demo-App/requirements.txt"

# Start services
#source /appdynamics/start.sh
su - appdynamics -c "source /appd/Python-Demo-App/start.sh"

exit 0
