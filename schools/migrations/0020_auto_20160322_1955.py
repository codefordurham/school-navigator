# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0019_auto_20160322_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='grade_max',
        ),
        migrations.RemoveField(
            model_name='school',
            name='grade_min',
        ),
        migrations.RemoveField(
            model_name='school',
            name='level',
        ),
        migrations.RemoveField(
            model_name='school',
            name='mission_statement',
        ),
        migrations.RemoveField(
            model_name='school',
            name='school_hours',
        ),
        migrations.RemoveField(
            model_name='school',
            name='website_url',
        ),
        migrations.RemoveField(
            model_name='school',
            name='year_round',
        ),
        migrations.RemoveField(
            model_name='schoolprofile',
            name='type',
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='grade_max',
            field=models.IntegerField(default=999),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='grade_min',
            field=models.IntegerField(default=-999),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='level',
            field=models.CharField(max_length=20, choices=[('elementary', 'Elementary'), ('middle', 'Middle'), ('secondary', 'Secondary'), ('high', 'High')]),
        ),
    ]
