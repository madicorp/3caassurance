from django import template

register = template.Library()
# TODO mettre dans fichier de config
email = 'contact@3caassurance.com'
phone = '+221 33 822 55 00'


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
    # TODO mettre dans fichier de config
    return {
        'email': email,
        'phone': phone,
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
        'email': email,
        'phone': phone,
        'parent': parent,
        'calling_page': calling_page,
        # required by the pageurl tag that we want to use within this template
        'request': context['request']
    }
