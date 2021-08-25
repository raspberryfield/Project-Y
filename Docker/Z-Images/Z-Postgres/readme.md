## Info about Postgres Docker Image
According to the official documentation, every script moved to **/docker-entrypoint-initdb.d/** in the docker image will be run on startup [https://hub.docker.com/_/postgres](#https://hub.docker.com/_/postgres). See how this is done in the Dockerfile.

## Useful commands

Build the z-postgres image:  
    `$ docker build -t z-postgres .`  

Run the image (stand alone):  
    $` docker run -p 5432:5432 --env-file ../../Env/postgres-variables.env z-postgres`  

Connect to the image (stand alone):  
    `$ psql -h 127.0.0.1 -p 5432 -U postgres`  

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



