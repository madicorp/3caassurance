from __future__ import absolute_import, unicode_literals

from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.wagtailcore.blocks import RichTextBlock
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.blocks import StructBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsearch import index


class ProductBlock(StructBlock):
    image = ImageChooserBlock()
    caption = RichTextBlock()


class HomePageProductBlock(StreamBlock):
    product = ProductBlock(label="Product", icon="pilcrow")


class HomePage(Page):
    products = StreamField(HomePageProductBlock())
    search_fields = Page.search_fields + [
        index.SearchField('products'),
    ]

    class Meta:
        verbose_name = "3CA Assurance"


HomePage.content_panels = [
    FieldPanel('title', classname="full title"),
    StreamFieldPanel('products')
]

HomePage.promote_panels = Page.promote_panels
