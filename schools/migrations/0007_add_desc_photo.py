# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0006_auto_20141206_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='school',
            name='photo',
            field=models.ImageField(null=True, upload_to=b''),
            preserve_default=True,
        ),
    ]
