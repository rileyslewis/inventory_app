# Using base image provided by nginx unit
FROM python:3.8
# Alternatively you can use different tags from https://hub.docker.com/r/nginx/unit
WORKDIR /backend

COPY ./backend/requirements.txt /backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

# server/backend/requirements.txt
COPY . /backend/server

# 
