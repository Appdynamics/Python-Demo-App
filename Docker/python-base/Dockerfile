FROM ubuntu

MAINTAINER Jeff Morgan (jeff.morgan@appdynamics.com)

################## BEGIN INSTALLATION ######################

# Add appdynamics user
RUN useradd --create-home appdynamics
RUN mkdir /appd
#RUN chown -R appdynamics.appdynamics /appdynamics

# Deploy libpam fix (allows cron to work)
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get -y build-dep pam
RUN export CONFIGURE_OPTS=--disable-audit && cd /root && apt-get -b source pam && dpkg -i libpam-doc*.deb libpam-modules*.deb libpam-runtime*.deb libpam0g*.deb

# Install packages
RUN apt-get update
RUN apt-get -y install postgresql
RUN apt-get -y install build-essential
RUN apt-get -y install locate
RUN updatedb
RUN apt-get -y install nmap
RUN apt-get -y install wget
RUN apt-get -y install zip
RUN apt-get -y install unzip
RUN apt-get -y install git
RUN apt-get -y install python-dev
RUN apt-get -y install postgresql
RUN apt-get -y install libpq-dev
RUN apt-get -y install postgresql-client
RUN apt-get -y install mysql-server
RUN apt-get -y install python-mysqldb
RUN apt-get -y install siege
ADD /distribute_setup.py /tmp/
RUN python /tmp/distribute_setup.py
RUN easy_install pip
RUN pip install virtualenv

##################### INSTALLATION END #####################
