# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0013_school_traditional_option_zone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reflexions',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('content', models.TextField(blank=True)),
                ('school', models.ForeignKey(to='schools.School')),
            ],
        ),
    ]
