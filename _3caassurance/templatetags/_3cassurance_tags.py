from django import template
from django.conf import settings
from django.core.urlresolvers import resolve
from django.core.urlresolvers import reverse
from django.utils import translation

register = template.Library()


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page


@register.inclusion_tag('_3caassurance/tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)
    return {
        'email': settings.CONTACT_EMAIL,
        'phone': settings.CONTACT_PHONE,
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request']
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('demo/tags/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.inclusion_tag('_3caassurance/tags/logo.html', takes_context=True)
def logo(context, parent, calling_page=None):
    return {
        'parent': parent,
        'calling_page': calling_page,
        # required by the pageurl tag that we want to use within this template
        'request': context['request']
    }


@register.inclusion_tag('_3caassurance/tags/footer.html', takes_context=True)
def footer(context, parent, calling_page=None):
    return {
        'email': settings.CONTACT_EMAIL,
        'phone': settings.CONTACT_PHONE,
        'parent': parent,
        'calling_page': calling_page,
        # required by the pageurl tag that we want to use within this template
        'request': context['request']
    }


# Thanks to http://stackoverflow.com/questions/11437454/django-templates-get-current-url-in-another-language
class TranslatedURL(template.Node):
    def __init__(self, language):
        self.language = language

    def render(self, context):
        view = resolve(context['request'].path)
        request_language = translation.get_language()
        translation.activate(self.language)
        url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        translation.activate(request_language)
        return url


@register.tag(name='translate_url')
def do_translate_url(parser, token):
    language = token.split_contents()[1]
    return TranslatedURL(language)


class HomeURL(template.Node):
    def render(self, context):
        return '/'.join(context['request'].path.split('/')[:2])


@register.tag(name='home_url')
def get_home_url(parser, token):
    return HomeURL()


@register.simple_tag(name='dynamic_trans', takes_context=True)
def dynamic_trans(context, obj, field_name):
    language = context['request'].path.split('/')[1]
    field_name_language = field_name + '_' + language
    return obj[field_name_language]
