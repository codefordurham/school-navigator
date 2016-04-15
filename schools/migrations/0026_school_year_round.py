# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0022_school_principal_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='year_round',
            field=models.BooleanField(default=False),
        ),
    ]
