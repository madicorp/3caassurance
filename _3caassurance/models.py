# coding=utf-8
from __future__ import absolute_import, unicode_literals

from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.wagtailcore.blocks import StreamBlock, DateBlock
from wagtail.wagtailcore.blocks import StructBlock
from wagtail.wagtailcore.blocks import TextBlock
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsearch import index


class SampleProductBlock(StructBlock):
    caption_fr = TextBlock(label='Titre FR')
    caption_en = TextBlock(label='Titre EN')
    description_fr = TextBlock(label='Description FR')
    description_en = TextBlock(label='Description EN')


class ProductBlock(SampleProductBlock):
    image = ImageChooserBlock()


class HomePageProductBlock(StreamBlock):
    product = ProductBlock(label='Product', icon='pilcrow')


class OfferBlock(SampleProductBlock):
    start_date = DateBlock(label='Date de début de validité de l\'offre')
    expire_date = DateBlock(label='Date d\'expiration de l\'offre')

    def __init__(self, *args, **kwargs):
        super(OfferBlock, self).__init__(*args, **kwargs)


class HomePageOfferBlock(StreamBlock):
    offer = OfferBlock(label='Offer', icon='pilcrow')


class HomePage(Page):
    products = StreamField(HomePageProductBlock())
    offers = StreamField(HomePageOfferBlock())
    search_fields = Page.search_fields + [
        index.SearchField('products'),
        index.SearchField('offers'),
    ]

    class Meta:
        verbose_name = '3CA Assurance'


HomePage.content_panels = [
    FieldPanel('title', classname='full title'),
    StreamFieldPanel('products'),
    StreamFieldPanel('offers')
]

HomePage.promote_panels = Page.promote_panels


class DeadlinePage(Page):
    deadline_file = DocumentChooserBlock()


class ContactPage(Page):
    pass


class EmployeeBlock(StructBlock):
    image = ImageChooserBlock()
    employee_name = TextBlock(label='Nom')
    position_fr = TextBlock(label='Poste FR')
    position_en = TextBlock(label='Poste EN')
    position_description_fr = TextBlock(label='Description de l\'employé FR', required=False)
    position_description_en = TextBlock(label='Description de l\'employé EN', required=False)


class AboutUsEmployeesBlock(StreamBlock):
    employee = EmployeeBlock(label='Employé', icon='user')


class AboutUsPage(Page):
    company_desc_fr = RichTextField(blank=False, verbose_name='Description de l\'entreprise FR', default='')
    company_desc_en = RichTextField(blank=False, verbose_name='Description de l\'entreprise EN', default='')
    employees = StreamField(AboutUsEmployeesBlock(), verbose_name='Employés')
    search_fields = Page.search_fields + [
        index.SearchField('company_desc_fr'),
        index.SearchField('company_desc_en'),
        index.SearchField('employees'),
    ]


AboutUsPage.content_panels = [
    FieldPanel('company_desc_fr', classname='full title'),
    FieldPanel('company_desc_en', classname='full title'),
    StreamFieldPanel('employees'),
]

AboutUsPage.promote_panels = Page.promote_panels
