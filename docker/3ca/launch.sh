#!/bin/bash

/usr/src/3ca/docker/3ca/wait-for-it.sh "$POSTGRES_1_PORT_5432_TCP_ADDR:$POSTGRES_1_PORT_5432_TCP_PORT" && \
python manage.py migrate --noinput && python manage.py loaddata user images _3caassurance && \
python manage.py update_index && python manage.py runserver 0.0.0.0:8000