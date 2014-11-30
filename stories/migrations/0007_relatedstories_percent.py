# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0006_auto_20141129_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatedstories',
            name='percent',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
