#!/bin/bash
source config.sh
REGISTRY_HOST=371275193966.dkr.ecr.eu-central-1.amazonaws.com
aws ecr get-login-password --region $AWS_REGION --profile $AWS_PROFILE | docker login --username AWS --password-stdin $REGISTRY_HOST
TAG=sim:latest
docker image tag $DOCKER_IMAGE $REGISTRY_HOST/$TAG
docker image push $REGISTRY_HOST/$TAG