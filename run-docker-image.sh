#!/bin/bash
CONTAINER_NAME=sim
docker rm $CONTAINER_NAME
WEBSERVER=127.0.0.1:5001
echo webserver will be accessible on docker host at: http://$WEBSERVER
docker run --name $CONTAINER_NAME -p $WEBSERVER:5000/tcp --attach STDOUT --attach STDERR sim:v1
