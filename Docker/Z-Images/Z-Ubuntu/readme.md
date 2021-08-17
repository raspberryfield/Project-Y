# Info about Z-Ubuntu  

## Docker
Build the image. (Must run the build command in this folder path `../Docker/Z-Images/Z-Ubuntu`):  
    `$ docker build -t z-ubuntu .`  

Get the conatiner ID of your z-ubuntu image by listing all conatiners (after you run docker compose):  
    `$ docker container ls --all`  

Use the image interactively, access a command prompt inside the running container:  
    `$ docker run -it --entrypoint /bin/bash z-ubuntu`  
>Note!
> The z-ubuntu image has an entrypoint defined, that is why you need to use it in the docker command, described above. Normally it is enough to use `$ docker run -it <docker_image_name> /bin/bash`.  

Exit interactive mode:  
    `# exit`  

Start container in interactively mode connected to a network (e.g. network z-net specified in docker compose file gives *docker_z-net* use `$ docker network ls`.):  
    `$ docker run -it --network=docker_z-net --entrypoint /bin/bash z-ubuntu`  

## Utility Apps
Browse the *Dockerfile* to see which applications that are added to the z-ubuntu image.

### Ping
See if host is available on network:  
    `# ping [ip][hostname]` e.g. `# ping z-postgres` (hostname z-postgres are resolved by the build in docker dns.)  

### DNS dnsutils  
Get IP address from dns name:  
    `# nslookup [hostname]` e.g. `# nslookup z-postgres` dns server will respond with answer resolve dns name to ip addres.  

### Psql - cmd tool for postgres
Get version:  
    `# psql --version`  
Connect to the postgres instance in docker container (z-net):  
    `# psql -h z-postgres -U postgres`  





