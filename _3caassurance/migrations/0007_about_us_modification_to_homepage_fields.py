# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 11:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0029_unicode_slugfield_dj19'),
        ('_3caassurance', '0006_homepage_offers'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='offers',
            field=wagtail.wagtailcore.fields.StreamField((('offer', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption_fr', wagtail.wagtailcore.blocks.TextBlock(label='Titre FR')), ('caption_en', wagtail.wagtailcore.blocks.TextBlock(label='Titre EN')), ('description_fr', wagtail.wagtailcore.blocks.TextBlock(label='Description FR')), ('description_en', wagtail.wagtailcore.blocks.TextBlock(label='Description EN'))), icon='pilcrow', label='Offer')),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='products',
            field=wagtail.wagtailcore.fields.StreamField((('product', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption_fr', wagtail.wagtailcore.blocks.TextBlock(label='Titre FR')), ('caption_en', wagtail.wagtailcore.blocks.TextBlock(label='Titre EN')), ('description_fr', wagtail.wagtailcore.blocks.TextBlock(label='Description FR')), ('description_en', wagtail.wagtailcore.blocks.TextBlock(label='Description EN'))), icon='pilcrow', label='Product')),)),
        ),
    ]