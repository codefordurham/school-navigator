# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0014_reflexions'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('speciality_type', models.TextField(blank=True, null=True)),
                ('phone_number', models.TextField(blank=True, null=True)),
                ('total_enrollment', models.IntegerField(null=True)),
                ('breakfast_served', models.NullBooleanField()),
                ('lunch_served', models.NullBooleanField()),
                ('points_of_pride', models.TextField(blank=True, null=True)),
                ('principal_name', models.TextField(blank=True, null=True)),
                ('principal_bio', models.TextField(blank=True, null=True)),
                ('principal_start_year', models.IntegerField(null=True)),
                ('extracurriculars', models.TextField(null=True)),
                ('courses_offered', models.TextField(null=True)),
                ('special_education', models.TextField(null=True)),
                ('gifted_education', models.TextField(null=True)),
                ('extended_care_start', models.TimeField(null=True)),
                ('extended_care_end', models.TimeField(null=True)),
                ('parental_involvement', models.TextField(null=True)),
                ('school', models.ForeignKey(to='schools.School')),
            ],
        ),
    ]
