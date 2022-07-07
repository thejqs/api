#!/bin/bash
python manage.py makemigrations
python manage.py migrate
uwsgi config/uwsgi.ini
