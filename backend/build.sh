#!/bin/bash

# Activate your virtual environment (if you're using one)
source backend/venv/Scripts/activate

# Install Python packages from requirements.txt
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Create a Django superuser
python manage.py createsuperuser --noinput \
  --username $DJANGO_SUPERUSER_USERNAME \
  --email $DJANGO_SUPERUSER_EMAIL \
  --first_name $DJANGO_SUPERUSER_FIRSTNAME \
  --last_name $DJANGO_SUPERUSER_LASTNAME \
  --password $DJANGO_SUPERUSER_PASSWORD