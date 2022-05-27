## Info about Superset Docker Image
Apache Superset is a datavisualization and explore tool.    

### Documentation  
- Docker hub - [https://hub.docker.com/r/apache/superset](https://hub.docker.com/r/apache/superset)  
- Apache Superset official documentation - [https://superset.apache.org/docs/intro/](https://superset.apache.org/docs/intro/)  
- Apache Superset github compose example - [https://github.com/apache/superset/blob/master/docker-compose.yml](https://github.com/apache/superset/blob/master/docker-compose.yml)

## Build command  
`$ docker build -t y-superset . ` 

## Additional Info   
The build script includes the download and init of example data. It might take a few minutes to finish.  
u/p admin, default setup.
The mount point should be used as /app.