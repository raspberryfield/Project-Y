## Info about Nginx docker image
Webserver and reverse proxy.

## Useful commands
Build the z-postgres image:  
    `$ docker build -t z-nginx .`  

Interactive mode with container:  
    `$ docker exec -it <container id> /bin/bash`  
exit interactive mode:  
    `# exit`  

## Test Nginx in Docker
The simpliest way to run the official nginx image:  
    `$ docker run -p 80:80 nginx`  
Now you can browse to localhost. If everything works fine, you should see a simple Welcome message in your browser. The text is from the nginx webserver.  


