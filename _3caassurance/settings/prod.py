from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['3caassurance-tiays.rhcloud.com']

SECRET_KEY = os.environ['OPENSHIFT_SECRET_TOKEN']

BASE_DIR = os.environ['OPENSHIFT_REPO_DIR']
PROJECT_DIR = os.path.join(BASE_DIR, '_3caassurance')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [os.path.join(PROJECT_DIR, 'static')]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_settings_export.settings_export',
            ],
        },
    },
]

try:
    from .local import *
except ImportError:
    pass
