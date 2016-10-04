# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_school_website_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='website_url',
            field=models.CharField(max_length=500),
        ),
    ]
