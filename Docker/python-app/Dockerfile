FROM appdynamics/python-base

MAINTAINER Jeff Morgan (jeff.morgan@appdynamics.com)

################## BEGIN INSTALLATION ######################

# Install app
RUN git clone https://github.com/Appdynamics/Python-Demo-App.git /appd/Python-Demo-App
ADD /appdynamics.cfg /appd/Python-Demo-App/
RUN chown -R appdynamics.appdynamics /appd
#ADD /siege.txt /appdynamics/Python-Demo-App/

# Add startup script
ADD /startup.sh /appd/
RUN chmod 777 /appd/startup.sh
ADD /env.sh /appd/
RUN chmod 777 /appd/env.sh
ADD /start.sh /appd/Python-Demo-App/
RUN chmod 777 /appd/Python-Demo-App/start.sh
RUN chown -R appdynamics.appdynamics /appd
#ADD /restartload.sh /appdynamics/Python-Demo-App/
#RUN chmod 777 /appdynamics/Python-Demo-App/restartload.sh

##################### INSTALLATION END #####################

# Expose Ports
EXPOSE 9000

CMD /appd/startup.sh && tail -F /var/log/dmesg
