# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0009_auto_20141130_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='entitytype',
            name='supertype',
            field=models.PositiveSmallIntegerField(blank=True, null=True, choices=[(0, b'Person'), (1, b'Place'), (2, b'Organization'), (3, b'Thing')]),
            preserve_default=True,
        ),
    ]
