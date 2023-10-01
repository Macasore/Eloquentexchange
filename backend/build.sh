#!/bin/bash

# Activate your virtual environment (if you're using one)
# source venv/Scripts/activate

# Install Python packages from requirements.txt
pip install -r requirements.txt
python create_superuser.py
# Apply database migrations

python manage.py migrate

# Create a Django superuser
