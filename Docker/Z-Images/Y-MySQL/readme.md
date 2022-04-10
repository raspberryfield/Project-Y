## Info about MySQL Docker Image
MySQL is a widely used, open-source relational database management system (RDBMS). Often referred as the most popular open source database. In Project-Y, it is mainly used as a source system that we want to read data FROM.  

### Documentation  
- Docker hub - [https://hub.docker.com/_/mysql](https://hub.docker.com/_/mysql)  
- MySQL official documentation - [https://dev.mysql.com/doc/](https://dev.mysql.com/doc/)  

## Build command  
`$ docker build -t y-mysql . ` 

## Run commands  
Run the image (stand alone, no compose command involved):  
    `$ docker run --name some-mysql --network y-net --env-file ../../Env/mysql-variables.env y-mysql`   
Here we are running mysql based on local image *y-mysql* and naming the container to *some-mysql*.  

> Tip! add **-d** to make the image run in container in detached mode in your terminal.  
> To stop container in detached mode, open another terminal and execute: `$ docker stop <container name>`.  


## Additional Info   
If you want to connect to your MySQL instance running in docker from your host, you most bind the ports between docker engine and your host. Run:  
    `$ docker run --name some-mysql -p 3306:3306 --network y-net --env-file ../../Env/mysql-variables.env y-mysql`   
Install mysql CLI (ubuntu):  
    `$ apt-get install -y mysql-client`  
Use mysql cli to connect to the instance running in docker:  
    `$ mysql --host=127.0.0.1 --port=3306 -u root --password mysql`  
Exit:
    `> exit`  

