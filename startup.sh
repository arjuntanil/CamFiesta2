#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Start Gunicorn
gunicorn --bind=0.0.0.0:8000 --timeout 600 --workers 2 camfiesta.wsgi:application
