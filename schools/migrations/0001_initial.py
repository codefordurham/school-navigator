# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=100)),
                ('level', models.IntegerField(choices=[(1, 'Elementary'), (2, 'Middle'), (3, 'Secondary'), (4, 'High')], default=4)),
                ('address', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=5)),
                ('magnet', models.BooleanField(default=False)),
                ('year_round', models.BooleanField(default=False)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('district', django.contrib.gis.db.models.fields.PolygonField(srid=4326, null=True)),
                ('walk_zone', django.contrib.gis.db.models.fields.PolygonField(srid=4326, null=True)),
                ('choice_zone', django.contrib.gis.db.models.fields.PolygonField(srid=4326, null=True)),
                ('priority_zone', django.contrib.gis.db.models.fields.PolygonField(srid=4326, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
