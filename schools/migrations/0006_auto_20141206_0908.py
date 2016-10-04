# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0005_auto_20141011_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='short_name',
            field=models.CharField(max_length=5, blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='school',
            name='level',
            field=models.CharField(choices=[('elementary', 'Elementary'), ('middle', 'Middle'), ('secondary', 'Secondary'), ('high', 'High')], max_length=20),
        ),
        migrations.AlterField(
            model_name='school',
            name='type',
            field=models.CharField(choices=[('neighborhood', 'Neighborhood'), ('magnet', 'Magnet'), ('charter', 'Charter'), ('specialty', 'Specialty')], max_length=20),
        ),
    ]
