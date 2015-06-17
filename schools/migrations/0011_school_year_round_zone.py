# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0010_add_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='year_round_zone',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326, blank=True, null=True),
            preserve_default=True,
        ),
    ]
