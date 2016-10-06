#!/bin/bash

BASEDIR=$(dirname "$0")
$BASEDIR/wait-for-it.sh "$POSTGRES_1_PORT_5432_TCP_ADDR:$POSTGRES_1_PORT_5432_TCP_PORT" && \
cat $BASEDIR/create_superuser.py | python manage.py shell && \
python manage.py migrate --noinput && python manage.py loaddata images _3caassurance && \
python manage.py update_index && python manage.py runserver 0.0.0.0:8000