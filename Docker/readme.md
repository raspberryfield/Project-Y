# Notes Docker
Docker images are central components in this project. Project-Y extends several official docker images. E.g. the docker image y-postgres extends the official postgres docker image with predefined example databses used in tutorials related to Project-Y.  
All images used in this project have the prefix **y-**.  
All images must be build locally. This is easiest done with the GUI or in each subfolder. There are build instructions and tips for each docker image in respectively subfolder in the **Y-Images** folder.  

## Docker Build  
1. Make sure that you run the script *pre-build-project-y.sh*. (You might need to give it execution permission: `chmod +x pre-build-project-y.sh`)  
2. Build each image with the GUI.  
3. After you build the images, run the script *post-build-project-y.sh*.  

> Tip! There are instructuions in each subfolder for the images, how to build and run them independently, if you encounter problem.  

## Docker Compose  
The difference between *docker* commands and *docker-compose* commands are that *docker-compose* aims at multiple containers/images at once, while *docker* handle single a container/image.  

Docker-compose is often used with one or multiple *docker-compose files*, it's like a config file for docker-compose.  

## Use the Browser to Interact with the Containers  
For each specified docker compose file, you will be able to interact with the following resources with your host's browser. Click the **info** button for each service to see the possible interaction endpoints.  
