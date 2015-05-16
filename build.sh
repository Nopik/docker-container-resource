#!/bin/bash

docker build --no-cache -t docker-container-resource .
docker tag -f docker-container-resource 192.168.59.103:5000/docker-container-resource
docker push 192.168.59.103:5000/docker-container-resource

