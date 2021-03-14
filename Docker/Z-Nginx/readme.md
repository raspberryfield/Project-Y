## Nginx
simpliest way to run the official nginx image:
(browse to localhost:80)
> $ docker run -p 80:80 nginx

## Interactive mode with container
> $ docker exec -it <container id> /bin/bash
> # exit

## build docker file
> $ docker build -t <name-webserver-image> .

## Manually edit /etc/hosts
> # The following lines are for project-Z
> 127.0.0.3       pgadmin pgadmin.local
