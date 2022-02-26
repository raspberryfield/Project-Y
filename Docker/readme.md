# Notes Docker
Docker images are central components in this project. Project-Z extends several official docker images. E.g. the docker image z-postgres extends the official postgres docker image with predefined example databses used in tutorials related to Project-Z.  
All images used in this project have the prefix **z-**.  
All images must be build locally. This is easiest done in each subfolder. There are build instructions and tips for each docker image in respectively subfolder in the **Z-Images** folder.  

## Docker Compose  
The difference between *docker* commands and *docker-compose* commands are that *docker-compose* aims at multiple containers/images at once, while *docker* handle single a container/image.  

Docker-compose is often used with one or multiple *docker-compose files*, it's like a config file for docker-compose. The main docker/compose file used is the **project-z-compose.yaml**.  

Run Docker Compose with File  
    `$ docker-compose -f project-z-compose.yaml up -d`  
**-d** - Run in detached mode in terminal.

