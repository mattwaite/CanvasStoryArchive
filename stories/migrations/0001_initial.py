# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entity_name', models.CharField(max_length=255)),
                ('entity_name_slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EntityType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entity_type', models.CharField(max_length=255)),
                ('entity_type_slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=255)),
                ('byline', models.CharField(max_length=255)),
                ('pubdate', models.DateTimeField()),
                ('description', models.TextField()),
                ('full_text', models.TextField()),
                ('word_count', models.IntegerField()),
                ('entities', models.ManyToManyField(to='stories.Entity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
