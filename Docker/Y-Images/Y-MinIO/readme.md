# About MinIO  
MinIO is used as the object store (platform for storing files for a lakehouse in Project-Y). MinIO is compatible with AWS S3.  

## Documentation  
- Docker Hub: [https://hub.docker.com/r/minio/minio/](https://hub.docker.com/r/minio/minio/).  
    - Erasure Code (very relevant reading for running in container with several volumes): [https://docs.min.io/docs/minio-erasure-code-quickstart-guide.html](https://docs.min.io/docs/minio-erasure-code-quickstart-guide.html).  
- MinIO quickstart guide docker: [https://docs.min.io/docs/minio-docker-quickstart-guide.html](https://docs.min.io/docs/minio-docker-quickstart-guide.html).  
- mc MinIO client: [https://docs.min.io/docs/minio-client-complete-guide.html](https://docs.min.io/docs/minio-client-complete-guide.html).  

## Endpoints  
- localhost:9000 - API.  
- localhost:9001 - Webbapp, called MinIO console.  
Browsing the end-points will all redirect to the console.  

## MinIO  
> Tip! The *access_key* can be referred as the user and the *secret_key* as the password.  

### Buckets  

## mc (MinIO CLI)  
The **mc** application is located in `/home/root`.  
Help:  
    `# ./mc --help`  
Connect:
    `./mc alias set <ALIAS> <YOUR-S3-ENDPOINT> [YOUR-ACCESS-KEY] [YOUR-SECRET-KEY] [--api API-SIGNATURE]`  
    e.g.:  
    `# ./mc alias set y-minio http://y-minio:9000 user@example.com password`  
Create a bucket:  
    `./mc mb <ALIAS>/<BUCKET NAME>`  
    e.g.:
    `./mc mb y-minio/test`  
List buckets:  
    `./mc ls <ALIAS>`  
