# Info about Y-Ubuntu  

## Docker
Build the image. (Must run the build command in this folder path `../Docker/Y-Images/Y-Ubuntu`):  
    `$ docker build -t y-ubuntu . `  

Get the conatiner ID of your y-ubuntu image by listing all conatiners (after you run docker compose):  
    `$ docker container ls --all`  

Use the image interactively, access a command prompt inside the running container:  
    `$ docker run -it --entrypoint /bin/bash y-ubuntu`  
>Note!
> The y-ubuntu image has an entrypoint defined, that is why you need to use it in the docker command, described above. Normally it is enough to use `$ docker run -it <docker_image_name> /bin/bash`.  

Exit interactive mode:  
    `# exit`  

Start container in interactively mode connected to a network (e.g. network y-net specified in docker compose file gives *docker_y-net* use `$ docker network ls`.):  
    `$ docker run -it --network=y-net --entrypoint /bin/bash y-ubuntu`  

## Utility Apps
Browse the *Dockerfile* to see which applications that are added to the y-ubuntu image.

### Ping
See if host is available on network:  
    `# ping [ip][hostname]` e.g. `# ping y-postgres` (hostname y-postgres are resolved by the build in docker dns.)  

### DNS dnsutils  
Get IP address from dns name:  
    `# nslookup [hostname]` e.g. `# nslookup y-postgres` dns server will respond with answer resolve dns name to ip addres.  

### Psql - cmd tool for postgres
Get version:  
    `# psql --version`  
Connect to the postgres instance in docker container (y-net):  
    `# psql -h y-postgres -U postgres`  

### MySQL - CLI  
Connect:  
    `# mysql --host y-mysql --password mysql`  
(This command will connect to database 'mysql' you will be asked to provide password. Mysql db holds user information etc. Don't put your data here.)  





