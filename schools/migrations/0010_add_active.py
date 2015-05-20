# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0009_auto_20150519_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='active',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
