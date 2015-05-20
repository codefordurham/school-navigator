# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0007_add_desc_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='hours',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='school',
            name='address',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='choice_zone',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='district',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='photo',
            field=models.ImageField(upload_to='', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='priority_zone',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='walk_zone',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='website_url',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='zip_code',
            field=models.CharField(max_length=5, blank=True),
        ),
    ]
