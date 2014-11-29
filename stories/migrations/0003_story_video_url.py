# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20141129_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='video_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
