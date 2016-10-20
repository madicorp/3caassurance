# coding=utf-8
from __future__ import absolute_import, unicode_literals

import uuid

from django.conf import settings
from django.core import mail
from django.core.mail.message import BadHeaderError, EmailMessage
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch.models import Query


def search(request):
    search_query = request.GET.get('query', None)
    page = request.GET.get('page', 1)

    # Search
    if search_query:
        search_results = Page.objects.live().search(search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return render(request, '_3caassurance/search.html', {
        'search_query': search_query,
        'search_results': search_results,
    })


def __send_contact_email(user_email, user_name, user_message, ref_num, connection):
    ref_str = '#%s' % ref_num
    contact_mail_ref = '%s : Contact de %s' % (ref_str, user_name)
    EmailMessage(subject=contact_mail_ref, from_email=settings.CONTACT_EMAIL,
                 body=user_message, to=[settings.CONTACT_EMAIL],
                 reply_to=[user_email], headers={'Sender': user_email},
                 connection=connection).send()


def __send_confirmation_email(user_email, user_name, user_message, ref_num, connection):
    confirmation_mail_ref = ugettext_lazy('#%s : Inquiry reception confirmation') % ref_num
    confirmation_mail_body_p1 = \
        ugettext_lazy('Dear %s,\n\nWe received your inquiry #%s and will answer soon.\n') % \
        (user_name, ref_num)
    confirmation_mail_body_p2 = \
        ugettext_lazy('Your inquiry:\n\n%s\n\nSincerely,\n\n3CA Team') % user_message
    EmailMessage(subject=confirmation_mail_ref, from_email=settings.CONTACT_EMAIL,
                 body=(confirmation_mail_body_p1 + confirmation_mail_body_p2), to=[user_email],
                 connection=connection).send()


@api_view(['POST'])
def post_message(request):
    if 'POST' == request.method:
        data = request.data
        try:
            with mail.get_connection() as connection:
                ref_num = uuid.uuid4()
                user_name = data['contact_name']
                user_message = data['message']
                user_email = data['contact_email']
                __send_contact_email(user_email, user_name, user_message, ref_num, connection)
                __send_confirmation_email(user_email, user_name, user_message, ref_num, connection)
        except BadHeaderError:
            # Headers injection prevention
            # https://docs.djangoproject.com/fr/1.10/topics/email/#preventing-header-injection
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)
