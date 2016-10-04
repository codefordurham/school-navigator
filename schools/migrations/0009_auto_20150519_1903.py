# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0008_auto_20150519_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='description',
            new_name='mission_statement',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='hours',
            new_name='school_hours',
        ),
    ]
