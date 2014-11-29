# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_story_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='entity_type',
            field=models.ForeignKey(blank=True, to='stories.EntityType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='headline_slug',
            field=models.SlugField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
