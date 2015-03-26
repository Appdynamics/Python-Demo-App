FROM appdynamics/python-base

MAINTAINER Jeff Morgan (jeff.morgan@appdynamics.com)

################## BEGIN INSTALLATION ######################

# Configure MySQL
RUN sed -i '/^bind-address/c\bind-address=0.0.0.0' /etc/mysql/my.cnf

# Add startup script
ADD /startup.sh /root/
RUN chmod 777 /root/startup.sh
RUN chown -R root.root /root/

##################### INSTALLATION END #####################

# Expose Ports
EXPOSE 3306
EXPOSE 22

CMD /root/startup.sh && tail -F /var/log/mysql/error.log
