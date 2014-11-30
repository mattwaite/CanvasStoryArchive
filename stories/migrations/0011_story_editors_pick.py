# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0010_entitytype_supertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='editors_pick',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
