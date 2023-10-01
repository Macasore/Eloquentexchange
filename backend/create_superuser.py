import os
import django
from django.contrib.auth import get_user_model

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auth_system.settings")
django.setup()

User = get_user_model()

# Define the superuser credentials here
username = os.getenv('DJANGO_SUPERUSER_FIRSTNAME')
email = os.getenv('DJANGO_SUPERUSER_EMAIL')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
firstname = os.getenv('DJANGO_SUPERUSER_FIRSTNAME')
lastname = os.getenv('DJANGO_SUPERUSER_LASTNAME')

# Create the superuser
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password, first_name=firstname, last_name=lastname)
    print('Superuser created successfully')
else:
    print('Superuser already exists')