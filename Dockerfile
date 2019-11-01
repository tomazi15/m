FROM node:8-alpine

RUN mkdir /basket
WORKDIR /basket

COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm install

COPY app app
COPY scripts scripts
