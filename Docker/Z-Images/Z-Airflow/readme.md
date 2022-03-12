## Info about Airflow Docker Image(s)
The Airflow Images(s) requires a different setup than the other images. Because, Airflow is simply not just ONE application that has been containerized.  
Airflow provides in the installation guide, a docker compose files with all services needed. Instead of adding all of these settings, I've decided to keep this compose file separately. I think it will be cleaner this way.  

This section from the apache/airflow dockerhub page might explain why airflow is so different. It tries to be an application and a library at the same time:  
> We publish Apache Airflow as apache-airflow package in PyPI. Installing it however might be sometimes tricky because Airflow is a bit of both a library and application. Libraries usually keep their dependencies open and applications usually pin them, but we should do neither and both at the same time. We decided to keep our dependencies as open as possible (in setup.py) so users can install different versions of libraries if needed. This means that from time to time plain pip install apache-airflow will not work or will produce unusable Airflow installation.

### Documentation  
- Docker "Quick Start" instructions - [https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html)  
- Apache Airflow official documentation - [https://airflow.apache.org/](https://airflow.apache.org/)  
- Apache Airflow Docker Hub - [https://hub.docker.com/r/apache/airflow](https://hub.docker.com/r/apache/airflow)  
- Airflow Custom Build Dockerfile - [https://airflow.apache.org/docs/docker-stack/build.html](https://airflow.apache.org/docs/docker-stack/build.html)  

## Build command  
No Dockerfile and build command for this image. Instead use the docker-compose file from Airflow.  

## Run Airflow  
All commands assumes that you are working from this directory.   

Create an environment file with the host id:  
    `$ echo -e "AIRFLOW_UID=$(id -u)" > .env`  
Init Airflow:  
    `$ docker-compose up airflow-init`  
You should in the end see the following message if it inits correctly:  
```
    airflow-init_1       | User "airflow" created with role "Admin"  
    airflow-init_1       | 2.2.4  
```  
Default: -u airflow -p airflow

After the Airflow init, you can run the compose file:  
    `$ docker-compose up`  

Stop Docker Compose:  
    `$ docker-compose down`  
Or cleanup environment:  
    `$ docker-compose down --volumes --rmi all`  

## Connect to Airflow  
Webinterface: `localhost:8080`  
    `user:airflow password: airflow`  

## About Airflow Docker Compose  
See [https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html) for latest updates.  

Download compose file:  
    `$ curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.4/docker-compose.yaml'`  
Create an environment file with the host id:  
    `$ echo -e "AIRFLOW_UID=$(id -u)" > .env`  

 > Tip! Docker Compose will automatically read environment variables if placed in a *.env* file. Read more about it here: [https://docs.docker.com/compose/environment-variables/](https://docs.docker.com/compose/environment-variables/).  

## Modifications to the Official Airflow Docker Compose Quick Start File  
Current version: 2.2.4  

