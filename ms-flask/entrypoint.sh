#!/bin/sh

if [ "$DATABASE" = "db_rrhh" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python run.py create_db

exec "$@"
