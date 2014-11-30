# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_auto_20141129_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedStories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.FloatField()),
                ('story1', models.ForeignKey(related_name='story1', to='stories.Story')),
                ('story2', models.ForeignKey(related_name='story2', to='stories.Story')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='story',
            name='related_stories',
        ),
    ]
