import os

from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@3caassurance.com', os.getenv('SITE_ADMIN_PWD'))
