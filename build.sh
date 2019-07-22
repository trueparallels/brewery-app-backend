#!/bin/bash

docker build . -t $ECR_URL:build-$CIRCLE_BUILD_NUM
docker push $ECR_URL:build-$CIRCLE_BUILD_NUM

docker tag $ECR_URL:build-$CIRCLE_BUILD_NUM $ECR_URL:latest
docker push $ECR_URL:latest