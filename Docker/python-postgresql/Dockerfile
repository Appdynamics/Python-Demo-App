FROM appdynamics/python-base

MAINTAINER Jeff Morgan (jeff.morgan@appdynamics.com)

ADD startup.sh /usr/local/bin/startup.sh
RUN chown postgres /usr/local/bin/startup.sh
RUN chmod 777 /usr/local/bin/startup.sh

################## BEGIN INSTALLATION ######################

# Run the rest of the commands as the ``postgres`` user created by the ``postgres-9.3`` package when it was ``apt-get installed``
USER postgres

# Create a PostgreSQL role named ``docker`` with ``docker`` as the password and
# then create a database `docker` owned by the ``docker`` role.
# Note: here we use ``&&\`` to run commands one after the other - the ``\``
#       allows the RUN command to span multiple lines.
RUN	/etc/init.d/postgresql start &&\
    psql --command "CREATE USER test WITH SUPERUSER PASSWORD 'test';" &&\
    createdb -O test test

# Adjust PostgreSQL configuration so that remote connections to the
# database are possible. 
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf

# And add ``listen_addresses`` to ``/etc/postgresql/9.3/main/postgresql.conf``
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf

##################### INSTALLATION END #####################

# Expose Ports
EXPOSE 5432
EXPOSE 22

CMD /usr/local/bin/startup.sh
