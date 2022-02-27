#!/bin/bash

docker build -t z-nginx ./Z-Images/Z-Nginx
docker build -t z-pgadmin ./Z-Images/Z-Pgadmin
docker build -t z-postgres ./Z-Images/Z-Postgres 
docker build -t z-ubuntu ./Z-Images/Z-Ubuntu 

