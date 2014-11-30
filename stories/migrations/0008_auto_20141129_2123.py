# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0007_relatedstories_percent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relatedstories',
            name='percent',
        ),
        migrations.RemoveField(
            model_name='relatedstories',
            name='score',
        ),
        migrations.AddField(
            model_name='relatedstories',
            name='countsum',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relatedstories',
            name='matchcount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relatedstories',
            name='story1count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
