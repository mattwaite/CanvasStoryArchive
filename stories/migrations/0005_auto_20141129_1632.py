# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_auto_20141129_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='NounCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('noun', models.CharField(max_length=255)),
                ('noun_count', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='story',
            name='nouns',
            field=models.ManyToManyField(to='stories.NounCount', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='related_stories',
            field=models.ManyToManyField(related_name='related_stories_rel_+', null=True, to='stories.Story', blank=True),
            preserve_default=True,
        ),
    ]
