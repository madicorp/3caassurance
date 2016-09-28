from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.core import mail
from django.core.mail.message import BadHeaderError, EmailMessage
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, render_to_response
from django.template import RequestContext
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


@api_view(['POST'])
def post_message(request):
    if 'POST' == request.method:
        data = request.data
        try:
            with mail.get_connection() as connection:
                EmailMessage(subject='Contact de ' + data['contact_name'], from_email=settings.CONTACT_EMAIL,
                             body=data['message'], to=[settings.CONTACT_EMAIL],
                             connection=connection,
                             reply_to=[data['contact_email']], headers={'Sender': data['contact_email']}).send()
        except BadHeaderError:
            # Headers injection prevention
            # https://docs.djangoproject.com/fr/1.10/topics/email/#preventing-header-injection
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_202_ACCEPTED)


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
