#!/bin/bash

# This is a script to start Bundy's MySQL server

# Start MySQL
service mysql start

# Create Databases
mysql -uroot -e "CREATE DATABASE test"

# Configure MySQL
mysql -uroot -e "CREATE USER 'test'@'%' IDENTIFIED BY 'test'" 
mysql -uroot -e "GRANT ALL PRIVILEGES on *.* to 'test'@'%'"
mysql -uroot -e "FLUSH PRIVILEGES"

# Restart MySQL
service mysql restart

exit 0
