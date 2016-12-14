# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0043_auto_20160908_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolprofile',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='submitted_at',
            field=models.DateTimeField(default=None, blank=True, null=True),
        ),
    ]
