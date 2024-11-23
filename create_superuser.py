import os
from django.contrib.auth import get_user_model
from django.db import IntegrityError
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")  # プロジェクト名に置き換え
django.setup()

User = get_user_model()

try:
    if not User.objects.filter(username=os.environ.get("DJANGO_SUPERUSER_USERNAME")).exists():
        User.objects.create_superuser(
            username=os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin"),
            email=os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com"),
            password=os.environ.get("DJANGO_SUPERUSER_PASSWORD", "adminpassword")
        )
        print("Superuser created successfully.")
    else:
        print("Superuser already exists.")
except IntegrityError as e:
    print(f"Failed to create superuser: {e}")
