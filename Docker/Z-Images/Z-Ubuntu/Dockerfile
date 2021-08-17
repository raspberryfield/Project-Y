FROM ubuntu
RUN apt-get update -y
# RUN apt-get install -y apt-utils # apt-utils not needed, safe to ignore errors.
RUN apt-get install -y iputils-ping
RUN apt-get install -y dnsutils
RUN apt-get install -y postgresql-client # psql client
ENTRYPOINT ["/bin/bash"]

