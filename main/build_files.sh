#!/bin/bash

echo "BUILD START"
 python3.11 -m pip install -r requirements.txt
 python3.11 -m pip install --upgrade pip --noinput

echo "Migrating Databases..."
 python3.11 manage.py makemigrations --noinput
 python3.11 manage.py migrate --noinput

 echo "Collecting Staticfiles..."
 python3.11 manage.py collectstatic --noinput --clear
