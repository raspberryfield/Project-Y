## Info about Pgadmin Docker Image
Pgadmin is a web-based IDE for postgres.   

### Documentation  
- Docker hub - [https://hub.docker.com/r/dpage/pgadmin4/](https://hub.docker.com/r/dpage/pgadmin4/)  
- pgadmin.org official documentation about the container - [https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html#](https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html#)  
    - Link to examples section: [https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html#examples](https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html#examples)  

## Build command  
`$ docker build -t z-pgadmin . ` 

## Post-Build  
> Warning: pgAdmin runs as the pgadmin user (UID: 5050) in the pgadmin group (GID: 5050) in the container. You must ensure that all files are readable, and where necessary (e.g. the working/session directory) writeable for this user on the host machine. For example: `sudo chown -R 5050:5050 <host_directory>`  

After you run the docker compose, so the volumes are created, run this:  
`$ sudo chown -R 5050:5050 /var/lib/docker/volumes/docker_project-z-data`  

## Connect to PostgreSQL
If you have followed the  

## Useful commands  
(If running stand-alone, make sure that you don't have a conflict on localhost, e.g. another container is also accepting requests as localhost.)  

Run the official image:  
    `docker run -p 80:80 -e 'PGADMIN_DEFAULT_EMAIL=user@domain.com' -e 'PGADMIN_DEFAULT_PASSWORD=secret' -d dpage/pgadmin4`  
You can browse pgadmin now by typing *localhost* in your browser.  

Run the z-pgadmin image:  
    `$ docker run -p 80:80 --env-file ../../Env/pgadmin-variables.env z-pgadmin`  
Using relative path to env-file so must be run from Z-Pgadmin folder.  

