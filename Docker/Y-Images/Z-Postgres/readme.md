## Info about Postgres Docker Image
According to the official documentation, every script ending with .sh and .sql moved to **/docker-entrypoint-initdb.d/** in the docker image will be run on startup [https://hub.docker.com/_/postgres](https://hub.docker.com/_/postgres). See how this is done in the Dockerfile.  

## Useful commands
> Note! Run the *create-docker-env.sh* script in the **Env** folder before trying these commands.  

Build the z-postgres image:  
    `$ docker build -t z-postgres . `  

Run this command and you will see two images created (postgres and z-postgres):  
    `$ docker image ls`  
One image is the official postgres docker image and the other one is the one produced by the build script that extends the official image.  

Run the image (stand alone, no compose command involved):  
    `$ docker run -p 5432:5432 --env-file ../../Env/postgres-variables.env z-postgres`  
> Tip! add **-d** to make the image run in container in detached mode in your terminal.  

Standard way of running the official image:  
`$ docker run -d --name my-postgres -p 5432:5432 -e POSTGRES_PASSWORD=<my_password> postgres`  
> Tip! Use \ and enter to create a new line in terminal.  

Connect interactively directly to the image:  
`$ docker exec -it z-postgres /bin/sh`

Make sure that the container is running:  
    `$ docker container ls`  

Connect to the image (stand alone, use client installed on your host):  
    `$ psql -h 127.0.0.1 -p 5432 -U postgres`  
Per default, postgres always creates a default users named *postgres*.  
Read more about the **psql** client in the wiki, section *IDEs and Tools*.  

List databases:  
    `# \l`  
    
Connect to db:  
    `# \c <name of db>`  
    
List tables in current db:  
    `# \dt`  
    
Example of SELECT:  
    `# SELECT * FROM names;`  

Exit postgres shell:  
    `# exit`  



