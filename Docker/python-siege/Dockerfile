FROM appdynamics/python-base

MAINTAINER Jeff Morgan (jeff.morgan@appdynamics.com)

################## BEGIN INSTALLATION ######################

ADD /siege.txt /appd/
ADD restartload.sh /appd/
RUN chmod 777 /appd/restartload.sh

# Setup Cron stuff
ADD /cron.conf /appd/
RUN crontab /appd/cron.conf

# Add startup / env script
ADD /startup.sh /appd/
RUN chmod 777 /appd/startup.sh
ADD /env.sh /appd/
RUN chmod 777 /appd/env.sh

##################### INSTALLATION END #####################

CMD /appd/startup.sh && tail -F /var/log/dmesg
