## Info about Airbyte
The team behind Airbyte presents it like the: "Open-source data integration for modern data teams. Get all your ELT data pipelines running in minutes, even your custom ones. Let your team focus on insights and innovation."  

Or in my words: It's an open source ETL tool with many pros. Enough pros that it made my top pick to represent ETL in this project.  

Note that Airbyte is similar to Airflow in the way that it consists of several components: redis, a scheduler, its own database etc. Therefore, just like with Airflow, I'll try to stick to the official docker-compose fiel as much as possible. 

### Documentation  
- Official website: [https://airbyte.com/](https://airbyte.com/)  
- Official getting started with airbyte locally guide: [https://docs.airbyte.com/quickstart/deploy-airbyte/](https://docs.airbyte.com/quickstart/deploy-airbyte/)  
- Airbyte open-source FAQ: [https://discuss.airbyte.io/c/faq/15](https://discuss.airbyte.io/c/faq/15)  
- Connector development: [https://docs.airbyte.com/connector-development/cdk-python/](https://docs.airbyte.com/connector-development/cdk-python/)  

## Build command  
No Dockerfile and build command for this image. Instead we are using the docker-compose file from Airbyte.  

## Run Airbyte  
All commands assumes that you are working from this directory.   

Start Docker Compose:  
    `$ docker-compose --env-file env.airbyte up`  
Stop Docker Compose:  
    `$ docker-compose --env-file env.airbyte down`  

In the terminal, when you see the banner *Airbyte* and this text: *http://localhost:8000/*, airbyte is ready.

## Connect to Airbyte  
Webinterface: `localhost:8000`  

## Modifications to the Official Airbyte Docker Compose Quick Start File  

At the end of the file, the y-net network configuration is added:  
```
networks:
  default:
    external:
      name: y-net
```  