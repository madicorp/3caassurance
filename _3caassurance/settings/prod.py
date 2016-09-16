from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['3caassurance-tiays.rhcloud.com']

SECRET_KEY = os.environ['OPENSHIFT_SECRET_TOKEN']

try:
    from .local import *
except ImportError:
    pass

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'static')
MEDIA_ROOT = os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'media')
STATICFILES_DIRS = [os.path.join(os.environ['OPENSHIFT_REPO_DIR'], '_3caassurance', 'static'),]
TEMPLATE_DIRS = (os.path.join(os.environ['OPENSHIFT_REPO_DIR'], '_3caassurance', 'templates'),)
