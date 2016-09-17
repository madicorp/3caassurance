from __future__ import absolute_import, unicode_literals

import logging

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

from _3caassurance import views as search_views
from _3caassurance import views

# Get an instance of a logger
logger = logging.getLogger(__name__)

urlpatterns = [
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^api/messages', views.post_message),
]

if not settings.DEBUG:
    logger.error('DEBUG %s', settings.DEBUG)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    url(r'^django-admin/', include(admin.site.urls)),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^search/$', search_views.search, name='search'),
    url(r'^(?!api)', include(wagtail_urls))
)

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
