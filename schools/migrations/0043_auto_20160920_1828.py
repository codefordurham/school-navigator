# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0042_remove_school_photo'),
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
