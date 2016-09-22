#!/usr/bin/env bash

pip install --upgrade pip && pip install -r requirements.txt
python ./manage.py compilemessages -l fr
./docker/3ca/launch.sh