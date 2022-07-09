FROM node:16-alpine3.12

# create destination directory
WORKDIR /app
COPY ./package*.json ./
COPY ./yarn.lock ./
RUN yarn