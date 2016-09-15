from django.utils.translation import ugettext_lazy as translate
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from _3caassurance.models import DeadlinePage


class DeadlinePageModelAdmin(ModelAdmin):
    model = DeadlinePage
    menu_label = translate('Deadline')
    menu_icon = 'date'
    menu_order = 200
    add_to_settings_menu = False


modeladmin_register(DeadlinePageModelAdmin)
