#!/bin/sh

function build_image {
  cat Dockerfile.tmplt | DJANGO_SETTINGS_MODULE="_3caassurance.settings.$1" envsubst > Dockerfile && docker build -t ekougs/3ca:$2 . && rm Dockerfile
}