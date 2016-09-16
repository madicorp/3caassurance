from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['3caassurance-tiays.rhcloud.com']

SECRET_KEY = os.environ['OPENSHIFT_SECRET_TOKEN']

try:
    from .local import *
except ImportError:
    pass

OPENSHIFT_PYTHON_URL = 'http://' + os.environ['OPENSHIFT_PYTHON_IP'] + ':' + os.environ['OPENSHIFT_PYTHON_PORT']

STATIC_URL = OPENSHIFT_PYTHON_URL + '/static/'
MEDIA_URL = OPENSHIFT_PYTHON_URL + '/media/'
STATIC_ROOT = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'static')
MEDIA_ROOT = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'media')
STATICFILES_DIRS = [os.path.join(os.environ['OPENSHIFT_REPO_DIR'], '_3caassurance', 'static'), ]
TEMPLATE_DIRS = (os.path.join(os.environ['OPENSHIFT_REPO_DIR'], '_3caassurance', 'templates'),)
