#!/bin/bash

# Activate your virtual environment (if you're using one)
# source venv/Scripts/activate

# Install Python packages from requirements.txt
pip install -r requirements.txt

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Create a Django superuser
python create_superuser.py