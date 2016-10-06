#!/bin/sh

function build_image {
  cat Dockerfile.tmplt | DJANGO_SETTINGS_MODULE="_3caassurance.settings.$1" envsubst > Dockerfile &&
  docker build -t ekougs/3ca:$2 . &&
  rm Dockerfile
}

function redeploy() {
  docker-compose stop &&
  docker-compose rm -f &&
  build_image $1 $2 &&
  cat dockerfile-compose.$1.tmplt | VERSION="$2" envsubst > dockerfile-compose.$1.yml &&
  docker-compose build &&
  DJANGO_SETTINGS_MODULE="_3caassurance.settings.$1" docker-compose up -f dockerfile-compose.$1.yml
}