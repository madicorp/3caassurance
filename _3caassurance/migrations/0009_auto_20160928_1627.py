# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-28 16:27
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('_3caassurance', '0008_about_us_company_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='offers',
            field=wagtail.wagtailcore.fields.StreamField([(b'offer', wagtail.wagtailcore.blocks.StructBlock([(b'caption_fr', wagtail.wagtailcore.blocks.TextBlock(label='Titre FR')), (b'caption_en', wagtail.wagtailcore.blocks.TextBlock(label='Titre EN')), (b'description_fr', wagtail.wagtailcore.blocks.TextBlock(label='Description FR')), (b'description_en', wagtail.wagtailcore.blocks.TextBlock(label='Description EN')), (b'start_date', wagtail.wagtailcore.blocks.DateBlock(label="Date de d\xe9but de validit\xe9 de l'offre")), (b'expire_date', wagtail.wagtailcore.blocks.DateBlock(label="Date d'expiration de l'offre"))], icon='pilcrow', label='Offer'))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='products',
            field=wagtail.wagtailcore.fields.StreamField([(b'product', wagtail.wagtailcore.blocks.StructBlock([(b'caption_fr', wagtail.wagtailcore.blocks.TextBlock(label='Titre FR')), (b'caption_en', wagtail.wagtailcore.blocks.TextBlock(label='Titre EN')), (b'description_fr', wagtail.wagtailcore.blocks.TextBlock(label='Description FR')), (b'description_en', wagtail.wagtailcore.blocks.TextBlock(label='Description EN')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock())], icon='pilcrow', label='Product'))]),
        ),
    ]
