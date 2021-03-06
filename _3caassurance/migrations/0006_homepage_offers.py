# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 09:59
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('_3caassurance', '0005_description_and_translation'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='offers',
            field=wagtail.wagtailcore.fields.StreamField([(b'offer', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption_fr', wagtail.wagtailcore.blocks.TextBlock(label='Titre FR')), (b'caption_en', wagtail.wagtailcore.blocks.TextBlock(label='Titre EN')), (b'description_fr', wagtail.wagtailcore.blocks.TextBlock(label='Description FR')), (b'description_en', wagtail.wagtailcore.blocks.TextBlock(label='Description EN'))], icon='pilcrow', label='Offer'))], default=[]),
            preserve_default=False,
        ),
    ]
