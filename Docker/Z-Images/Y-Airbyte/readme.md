## Info about Airbyte
The team behind Airbyte presents it like the: "Open-source data integration for modern data teams. Get all your ELT data pipelines running in minutes, even your custom ones. Let your team focus on insights and innovation."  

Or in my words: It's an open source ETL tool with many pros. Enough pros that it made my top pick to represent ETL in this project.  

Note that Airbyte is similar to Airflow in the way that it consists of several components: redis, a scheduler, its own database etc. Therefore, just like with Airflow, I'll try to stick to the official docker-compose fiel as much as possible. 

### Documentation  
- Official website: [https://airbyte.com/](https://airbyte.com/)  
- Official getting started with airbyte locally guide: [https://docs.airbyte.com/quickstart/deploy-airbyte/](https://docs.airbyte.com/quickstart/deploy-airbyte/)  
- Airbyte open-source FAQ: [https://discuss.airbyte.io/c/faq/15](https://discuss.airbyte.io/c/faq/15)  
- Connector development: [https://docs.airbyte.com/connector-development/cdk-python/](https://docs.airbyte.com/connector-development/cdk-python/)  

NOTES:

docker-compose --env-file env.airbyte up 
docker-compose --env-file env.airbyte down  

/   |  (_)____/ /_  __  __/ /____
airbyte-server      |   / /| | / / ___/ __ \/ / / / __/ _ \
airbyte-server      |  / ___ |/ / /  / /_/ / /_/ / /_/  __/
airbyte-server      | /_/  |_/_/_/  /_.___/\__, /\__/\___/
airbyte-server      |                     /____/
airbyte-server      | --------------------------------------
airbyte-server      |  Now ready at http://localhost:8000/
airbyte-server      | --------------------------------------




## Build command  
`$ docker build -t y-mysql . ` 

## Run commands  
Run the image (stand alone, no compose command involved):  
    `$ docker run --name some-mysql --network y-net --env-file ../../Env/mysql-variables.env y-mysql`   
Here we are running mysql based on local image *y-mysql* and naming the container to *some-mysql*.  

> Tip! add **-d** to make the image run in container in detached mode in your terminal.  
> To stop container in detached mode, open another terminal and execute: `$ docker stop <container name>`.  

## Interactive
Connect interactively directly to the image:  
    `$ docker exec -it some-mysql /bin/sh`  

## Additional Info   
If you want to connect to your MySQL instance running in docker from your host, you most bind the ports between docker engine and your host. Run:  
    `$ docker run --name some-mysql -p 3306:3306 --network y-net --env-file ../../Env/mysql-variables.env y-mysql`   
Install mysql CLI (ubuntu):  
    `$ apt-get install -y mysql-client`  
Use mysql cli to connect to the instance running in docker:  
    `$ mysql --host=127.0.0.1 --port=3306 -u root --password mysql`  
Exit:
    `> exit`  

Example databases:  
* [https://dev.mysql.com/doc/index-other.html](https://dev.mysql.com/doc/index-other.html)  
* [https://www.mysqltutorial.org/mysql-sample-database.aspx](https://www.mysqltutorial.org/mysql-sample-database.aspx)  
* [https://sourceforge.net/projects/awmysql/](https://sourceforge.net/projects/awmysql/) 

