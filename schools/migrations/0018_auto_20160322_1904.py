# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0017_submitted_at_null'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolprofile',
            name='grade_max',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='grade_min',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='level',
            field=models.CharField(max_length=20, choices=[('elementary', 'Elementary'), ('middle', 'Middle'), ('secondary', 'Secondary'), ('high', 'High')], blank=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='mission_statement',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='school_hours',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='type',
            field=models.CharField(max_length=20, choices=[('neighborhood', 'Neighborhood'), ('magnet', 'Magnet'), ('charter', 'Charter'), ('speciality', 'Specialty')], blank=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='website_url',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='year_round',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='submitted_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
