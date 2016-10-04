# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0021_auto_20160414_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='principal_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
