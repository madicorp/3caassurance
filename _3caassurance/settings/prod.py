from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['3caassurance-tiays.rhcloud.com', ]

SECRET_KEY = os.environ['OPENSHIFT_SECRET_TOKEN']

try:
    from .local import *
except ImportError:
    pass

MEDIA_ROOT = os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'media')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'debug.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
