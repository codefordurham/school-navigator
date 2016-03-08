# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0015_schoolprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolprofile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(1900, 1, 1, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='submitted_at',
            field=models.DateTimeField(default=datetime.datetime(1900, 1, 1, 0, 0)),
            preserve_default=False,
        ),
    ]
