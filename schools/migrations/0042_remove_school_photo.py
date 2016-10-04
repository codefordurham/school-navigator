# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0041_auto_20160726_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='photo',
        ),
    ]
