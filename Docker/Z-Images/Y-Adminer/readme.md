## Info about Adminer Docker Image
From Docker Hub:  
Adminer (formerly phpMinAdmin) is a full-featured database management tool written in PHP. Conversely to phpMyAdmin, it consist of a single file ready to deploy to the target server. Adminer is available for MySQL, PostgreSQL, SQLite, MS SQL, Oracle, Firebird, SimpleDB, Elasticsearch and MongoDB.  

In Project-Y, Adminer is mainly used as a webbased IDE for MySQL.  

### Documentation  
- Docker hub - [https://hub.docker.com/_/mysql](https://hub.docker.com/_/mysql)  
- Adminer official documentation - [https://www.adminer.org/](https://www.adminer.org/)  

## Build command  
`$ docker build -t y-adminer . ` 

## Run commands  
Run the image (stand alone, no compose command involved):  
    `$ docker run --name my-adminer -p 8080:8080 --network y-net y-adminer`   
Here we are running adminer based on local image *y-adminer* and naming the container to *my-adminer* and connecting to already created network *y-net*.  

> Tip! use **-d** as an optional command to make the image run in container in detached mode in your terminal.  
> To stop container in detached mode, open another terminal and execute: `$ docker stop <container name>`.  

You can now browse to:  
`http://localhost:8080`  

## Interactive
Connect interactively directly to the image:  
    `$ docker exec -it my-adminer /bin/sh`  

## Using Adminer in Project-Y  
Open you host webbrowser and browse to either:  
    - localhost:8005  

**MySQL**
| Column | Value |
| -------| ----- |
| System  | MySQL  |
| Server | y-mysql|
| Username | root |
| Password | the value you entered in the env file |
| Database | mysql |

**PostgreSQL**
| Column | Value |
| -------| ----- |
| System  | PostgreSQL  |
| Server | z-postgres|
| Username | postgres |
| Password | the value you entered in the env file |
| Database | postgres |

## Additional Info   
Adminer as-is in Project-Y has only been tested with MySQL and PostgreSQL. But it should be possible to use it with:  
- MySQL
- PostgreSQL
- SQLite
- SimpleDB
- Elasticsearch  

### How to connect to MySQL stand alone. 
If you followed the instruction under Z-MySQL how to start a mysql instance standalone, you can connect to that standalone with adminer.

After you run:  
    `$ docker run --name some-mysql -p 3306:3306 --network y-net --env-file ../../Env/mysql-variables.env y-mysql`   
You may now run the standalone command for adminer:  
    `$ docker run --name my-adminer -p 8080:8080 --network y-net y-adminer`  
Now open in your browser:  
    `http://localhost:8080`  

In the login form, enter these values:  

| Column | Value |
| -------| ----- |
| System  | MySQL  |
| Server | some-mysql (name of container)|
| Username | root |
| Password | the value you entered in the env file |
| Database | mysql |
