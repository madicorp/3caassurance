"""
WSGI config for _3caassurance project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

from __future__ import absolute_import, unicode_literals

import os

from django.core.wsgi import get_wsgi_application

if os.getenv("OPENSHIFT_REPO_DIR") is not None:
    env_settings = "_3caassurance.settings.prod"
else:
    env_settings = "_3caassurance.settings.dev"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", env_settings)

application = get_wsgi_application()
