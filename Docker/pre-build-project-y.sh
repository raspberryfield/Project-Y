# all images depends on the network 'y-net'
docker network create -d bridge y-net

# Airflow needs the user id.
echo -e "AIRFLOW_UID=$(id -u)" > ./Y-Images/Y-Airflow/.env
# Init Airflow
docker-compose -f ../Docker/Y-Images/Y-Airflow/docker-compose-airflow.yaml up airflow-init