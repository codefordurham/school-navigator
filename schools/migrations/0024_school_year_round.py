# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0023_auto_20160415_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='year_round',
            field=models.BooleanField(default=False),
        ),
    ]
