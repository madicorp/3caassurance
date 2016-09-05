from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

SECRET_KEY = os.environ['OPENSHIFT_SECRET_TOKEN']

try:
    from .local import *
except ImportError:
    pass

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'wsgi', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'wsgi', 'static', 'media')
STATICFILES_DIRS = (os.path.join(BASE_DIR, '_3caassurance', 'static'),)
TEMPLATE_DIRS = (os.path.join(BASE_DIR, '_3caassurance', 'templates'),)
