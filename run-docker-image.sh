#!/bin/bash
source config.sh
docker rm $CONTAINER_NAME
WEBSERVER=127.0.0.1:5001
echo webserver will be accessible on docker host at: http://$WEBSERVER
docker run --name $CONTAINER_NAME -p $WEBSERVER:5000 --attach STDOUT --attach STDERR -it $DOCKER_IMAGE
