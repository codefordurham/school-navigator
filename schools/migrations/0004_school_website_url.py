# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0003_school_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='website_url',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
