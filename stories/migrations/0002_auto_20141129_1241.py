# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entity',
            options={'verbose_name_plural': 'entities'},
        ),
        migrations.AlterModelOptions(
            name='story',
            options={'verbose_name_plural': 'stories'},
        ),
        migrations.AddField(
            model_name='story',
            name='large_image_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='small_image_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
