# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0035_auto_20160428_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='photo',
            field=models.ImageField(upload_to='school_photos/', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='year_opened',
            field=models.IntegerField(null=True, help_text='In what year was your school opened?', blank=True),
        ),
    ]
