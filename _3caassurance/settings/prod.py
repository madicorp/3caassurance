from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = True
ALLOWED_HOSTS = ['3caassurance-tiays.rhcloud.com', ]

SECRET_KEY = os.environ['OPENSHIFT_SECRET_TOKEN']

try:
    from .local import *
except ImportError:
    pass
