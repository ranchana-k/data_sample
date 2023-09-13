# data_sample
## Objective
To write data read from parguet files to Postgresql Database

## How it works
When running docker-compose.yaml file, three containers will be created including :
1) Postgresql Database
2) Mage.ai Pipeline which will process files and write data to database
3) App which run the script to generate .parguet files in folder data_sample

## Prerequisites:
1. Docker Desktop
2. Postgresql local database 

## How to deploy 
1. Open Docker Desktop
2. clone git and run command `docker-compose up -d` in CLI 
3. Open https://localhost:6789 to see Mage.ai pipelines

## File Description
- `app` includes sampledata_new.py script to generate data and Dockerfile for container running this script
- `test_project` all files related to Mage.ai Pipelines
- `Dockerfile` for a container of Mage.ai Pipelines
- `docker-compose.yaml` files to run all containers including postgres container, mage_pipeline container and app container.

