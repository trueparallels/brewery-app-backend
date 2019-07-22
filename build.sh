#!/bin/bash

docker build . -t $ECR_URL:latest

# IMAGE_ID=$(docker images --filter=reference='brewery-app-backend:latest' --format "{{.ID}}")

docker tag $ECR_URL:build-$CIRCLE_BUILD_NUM $ECR_URL:latest
docker push $ECR_URL:latest