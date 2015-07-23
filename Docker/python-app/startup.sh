#!/bin/bash

# This is a starup script for the Python Demo app

# Set EC2 Region variable
source /appd/env.sh && sed -i "/^host/c\host = ${CONTROLLER}" /appd/Python-Demo-App/appdynamics.cfg
source /appd/env.sh && sed -i "/^port/c\port = ${APPD_PORT}" /appd/Python-Demo-App/appdynamics.cfg
source /appd/env.sh && sed -i "/^ssl/c\ssl = ${SSL}" /appd/Python-Demo-App/appdynamics.cfg
source /appd/env.sh && sed -i "/^account/c\account = ${ACCOUNT_NAME}" /appd/Python-Demo-App/appdynamics.cfg
source /appd/env.sh && sed -i "/^accesskey/c\accesskey = ${ACCESS_KEY}" /appd/Python-Demo-App/appdynamics.cfg
sed -i 's/localhost/python_mysql/g' /appd/Python-Demo-App/demo/config.py
sed -i 's/127.0.0.1/python_postgres/g' /appd/Python-Demo-App/demo/config.py
chown -R appdynamics.appdynamics /appd

# Setup virtualenv
su - appdynamics -c "virtualenv /appd/Python-Demo-App/env"
su - appdynamics -c "/appd/Python-Demo-App/env/bin/pip install --pre appdynamics"
su - appdynamics -c "/appd/Python-Demo-App/env/bin/pip install --allow-external mysql-connector-python -r /appd/Python-Demo-App/requirements.txt"
su - appdynamics -c "/appd/Python-Demo-App/env/bin/pip install -r /appd/Python-Demo-App/requirements.txt"

# Start services
su - appdynamics -c "source /appd/Python-Demo-App/start.sh"

