# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0008_auto_20141129_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='guid',
            field=models.CharField(max_length=64, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='link',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
