# Some info about Nginx
Webserver and reverse proxy.

## Test Nginx in Docker
The simpliest way to run the official nginx image:  
    `$ docker run -p 80:80 nginx`  
Now you can browse to localhost. If everything works fine, you should see a simple Welcome message in your browser. The text is from the nginx webserver.  

## Interactive mode with container
> $ docker exec -it <container id> /bin/bash
> # exit

## build docker file
> $ docker build -t <name-webserver-image> .

## Manually edit /etc/hosts
> # The following lines are for project-Z
> 127.0.0.3       pgadmin pgadmin.local
