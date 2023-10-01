from django.contrib.auth import get_user_model
import os

User = get_user_model()

# Define the superuser credentials here
username = os.getenv('DJANGO_SUPERUSER_FIRSTNAME')
email = os.getenv('DJANGO_SUPERUSER_EMAIL')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
firstname = os.getenv('DJANGO_SUPERUSER_FIRSTNAME')
lastname = os.getenv('DJANGO_SUPERUSER_LASTNAME')

# Create the superuser
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, firstname, lastname, password)
