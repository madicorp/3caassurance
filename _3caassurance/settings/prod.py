from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['3caassurance-tiays.rhcloud.com']

SECRET_KEY = os.environ['OPENSHIFT_SECRET_TOKEN']

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'media')
STATICFILES_DIRS = [os.path.join(PROJECT_DIR, 'static')]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # TODO before delivery
    # 'handlers': {
    #     'mail_admins': {
    #         'level': 'ERROR',
    #         'class': 'django.utils.log.AdminEmailHandler'
    #     }
    # },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from .local import *
except ImportError:
    pass
