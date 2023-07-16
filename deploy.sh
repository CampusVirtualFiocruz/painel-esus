#!/bin/bash

sudo docker-compose build
sudo docker-compose up -d
sudo docker exec bd /restore.sh