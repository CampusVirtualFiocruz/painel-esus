#!/bin/bash

docker kill painel-front-container
docker rm painel-front-container
docker build -t painel-front .
docker run -d -p 5002:80 --name painel-front-container painel-front