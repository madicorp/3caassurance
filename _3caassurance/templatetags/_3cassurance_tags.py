from django import template
from django.conf import settings
from django.utils.translation import get_language
from datetime import datetime
from operator import is_not
from functools import partial

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


@register.simple_tag(name='dynamic_trans', takes_context=True)
def dynamic_trans(context, obj, field_name, get_lang_fn=get_language):
    field_name_language = field_name + '_' + get_lang_fn()
    try:
        # For django models
        return getattr(obj, field_name_language)
    except AttributeError:
        # For wagtail StructValue
        return obj[field_name_language]


@register.simple_tag(name='first_name', takes_context=True)
def first_name(context, complete_name):
    return ' '.join(complete_name.split()[:-1])


@register.simple_tag(name='surname', takes_context=True)
def surname(context, complete_name):
    return complete_name.split()[-1]


@register.filter(name='active_offers')
def active_offers(offers):
    print repr(offers)
    present = datetime.now().date()
    active_offers = map(lambda
                            offer: None if offer.value['start_date'] > present or offer.value['expire_date'] < present else offer,
                        offers)
    print repr(active_offers)
    return filter(partial(is_not, None), active_offers)
