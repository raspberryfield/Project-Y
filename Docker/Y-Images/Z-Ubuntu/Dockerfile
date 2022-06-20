FROM ubuntu
RUN apt-get update -y
# Utils -y [yes]
RUN apt-get install -y iputils-ping
RUN apt-get install -y dnsutils
RUN apt-get install -y postgresql-client # psql client
RUN apt-get install -y mysql-client


# SFTP
# reference: https://linuxhint.com/setup-sftp-server-ubuntu/
# install ssh service. (Note, if you use this for something else than just SFTP file server, it is consider bad practice in docker.)
RUN apt-get install -y openssh-server
# ssh settings added to the global ssh service config file.
RUN echo 'Match group sftp' >> /etc/ssh/sshd_config
RUN echo 'ChrootDirectory /home' >> /etc/ssh/sshd_config
RUN echo 'X11Forwarding no' >> /etc/ssh/sshd_config
RUN echo 'AllowTcpForwarding no' >> /etc/ssh/sshd_config
RUN echo 'ForceCommand internal-sftp' >> /etc/ssh/sshd_config
# create sftp group and user. Set password.
RUN addgroup sftp
RUN useradd -m sftp_user -g sftp
# 'sftp' being the password
RUN echo 'sftp_user:sftp' | chpasswd
# grant permission
RUN chmod 700 /home/sftp_user/





ENTRYPOINT ["/bin/bash"]

