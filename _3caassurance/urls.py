from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

from _3caassurance import views as search_views
from _3caassurance.deadlines import send_deadlines


@api_view(['POST'])
def handle_messages(request):
    if 'POST' == request.method:
        data = request.data
        send_mail(subject='Enquiry from ' + data['contact_name'],
                  from_email=settings.CONTACT_EMAIL,
                  message=data['message'],
                  recipient_list=[settings.CONTACT_EMAIL, data['contact_email']])
        return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def handle_deadlines(request):
    if 'POST' == request.method:
        send_deadlines(request.FILES['deadline_file'])
        return Response(status=status.HTTP_202_ACCEPTED)


urlpatterns = [
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^api/messages', handle_messages),
    url(r'^api/deadlines', handle_deadlines),
]

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
