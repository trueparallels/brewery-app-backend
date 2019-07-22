#!/bin/bash

docker build . -t brewery-app-backend:latest

IMAGE_ID = $(docker images --filter=reference='brewery-app-backend:latest' --format "{{.ID}}")

docker tag $IMAGE_ID $ECR_URL:build-$CIRCLE_BUILD_NUM $ECR_URL:latest
docker push $ECR_URL:latest