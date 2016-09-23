# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 21:26
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('_3caassurance', '0007_about_us_modification_to_homepage_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutuspage',
            name='company_desc_en',
            field=wagtail.wagtailcore.fields.RichTextField(default='', verbose_name="Description de l'entreprise EN"),
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='company_desc_fr',
            field=wagtail.wagtailcore.fields.RichTextField(default='', verbose_name="Description de l'entreprise FR"),
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='employees',
            field=wagtail.wagtailcore.fields.StreamField([(b'employee', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'employee_name', wagtail.wagtailcore.blocks.TextBlock(label='Nom')), (b'position_fr', wagtail.wagtailcore.blocks.TextBlock(label='Poste FR')), (b'position_en', wagtail.wagtailcore.blocks.TextBlock(label='Poste EN')), (b'position_description_fr', wagtail.wagtailcore.blocks.TextBlock(label="Description de l'employ\xe9 FR", required=False)), (b'position_description_en', wagtail.wagtailcore.blocks.TextBlock(label="Description de l'employ\xe9 EN", required=False))], icon='user', label='Employ\xe9'))], default=None, verbose_name='Employ\xe9s'),
            preserve_default=False,
        ),
    ]
