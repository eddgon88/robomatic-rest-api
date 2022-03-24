## Running application in docker containers:
#### Using Docker CLI
```
docker network ls
docker network create --driver bridge micro_network (skip if already created)
docker build -t rest-api-srv .
docker run -p 8001:8001 --detach --name rest-api-service --net=micro_network rest-api-srv
```