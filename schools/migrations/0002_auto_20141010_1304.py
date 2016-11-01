# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='level',
        ),
        migrations.RemoveField(
            model_name='school',
            name='magnet',
        ),
        migrations.AddField(
            model_name='school',
            name='grade_max',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='grade_min',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='type',
            field=models.CharField(default='unset', max_length=20, choices=[(b'neighborhood', b'Neighborhood'), (b'magnet', b'Magnet'), (b'charter', b'Charter'), (b'speciality', b'Specialty')]),
            preserve_default=False,
        ),
    ]
