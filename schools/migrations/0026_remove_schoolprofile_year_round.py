# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0025_auto_20160415_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolprofile',
            name='year_round',
        ),
    ]
