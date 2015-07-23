FROM appdynamics/python-base

MAINTAINER Jeff Morgan (jeff.morgan@appdynamics.com)

################## BEGIN INSTALLATION ######################

ADD /siege.txt /appd/

# Add startup / env script
ADD /startup.sh /appd/
RUN chmod 777 /appd/startup.sh
ADD /env.sh /appd/
RUN chmod 777 /appd/env.sh

##################### INSTALLATION END #####################

CMD /appd/startup.sh
