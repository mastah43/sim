#!/bin/bash
source docker-sim-config.sh
docker rm ${CONTAINER_NAME}
WEBSERVER_PORT=5001
WEBSERVER=127.0.0.1:${WEBSERVER_PORT}
echo webserver will be accessible on docker host at: http://${WEBSERVER}
docker run --name ${CONTAINER_NAME} --publish ${WEBSERVER_PORT}:5000 --attach STDOUT --attach STDERR ${DOCKER_IMAGE}
