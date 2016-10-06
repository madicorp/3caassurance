from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False
SECRET_KEY = os.environ['SECRET_TOKEN']
ALLOWED_HOSTS = ['3caassurance.com', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_USER'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_1_PORT_5432_TCP_ADDR'),
        'PORT': os.getenv('POSTGRES_1_PORT_5432_TCP_PORT')
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.com'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = CONTACT_EMAIL
EMAIL_HOST_PASSWORD = os.getenv('CONTACT_EMAIL_PASSWORD')
