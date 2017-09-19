# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0043_auto_20160920_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schoolprofile',
            old_name='speciality_type',
            new_name='specialty_type',
        ),
        migrations.AlterField(
            model_name='school',
            name='type',
            field=models.CharField(choices=[('neighborhood', 'Neighborhood'), ('magnet', 'Magnet'), ('charter', 'Charter'), ('specialty', 'Specialty')], max_length=20),
        ),
    ]
