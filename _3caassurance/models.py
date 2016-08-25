from __future__ import absolute_import, unicode_literals

from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.blocks import RichTextBlock
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.blocks import StructBlock
from wagtail.wagtailcore.blocks import TextBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsearch import index


class HomePage(Page):
    pass


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = TextBlock('title')
    title = RichTextBlock()


class ImageStreamBlock(StreamBlock):
    image = ImageBlock(label='Photo', icon='image')


class PhotoGalleryPage(Page):
    body = StreamField(ImageStreamBlock())

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    class Meta:
        verbose_name = 'Gallerie Photos'

PhotoGalleryPage.content_panels = [
    FieldPanel('title', classname='full title'),
    StreamFieldPanel('body')
]

PhotoGalleryPage.promote_panels = Page.promote_panels
