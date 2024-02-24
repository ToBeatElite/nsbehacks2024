#### Setup from Docker

```
# create network used by the containers

docker network create app_network

# OPTIONAL delete every running container

docker rm -v -f $(docker ps -qa)
```

#### Running with Docker

```
# for production env

docker-compose -f docker_configs/docker-compose.prod.yml up --build

# for dev env

docker-compose -f docker_configs/docker-compose.dev.yml up --build

```