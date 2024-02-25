#### Files Setup

you must create a .env.prodution.local file in the project root with 3 values

```
ENV_VARIABLE=?
NEXT_PUBLIC_ENV_VARIABLE=?
DJANGO_SECRET_KEY=?
```

do not run this software in production or public environments


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