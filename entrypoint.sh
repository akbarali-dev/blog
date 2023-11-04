#!/bin/bash

if [ "$DATABASE" = "blog_db" ]
then
  echo "Waiting for postgres..."

  while ! nc -z $SQL_HOST $SQL_PORT; do
   sleep 0.1
  done

  echo "PostgreSQL started"
fi

sleep 2

echo "Apply database migrations"
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py migrate auth



echo "create admin"
python3 manage.py create_admin
python3 manage.py create-admin

echo "Starting server"
python3 manage.py runserver --insecure 0.0.0.0:8000

exec "$@"







##!/bin/bash
#
#sleep 10
#python3 manage.py migrate
#python3 manage.py runserver 0.0.0.0:8000

