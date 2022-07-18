#!/bin/bash
python manage.py migrate
uwsgi config/uwsgi.ini
