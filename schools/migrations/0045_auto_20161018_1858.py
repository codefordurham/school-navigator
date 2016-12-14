# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0044_auto_20160920_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='principal_email',
            field=models.CharField(help_text='Email of Principal (may also reach Superintendent)', max_length=100, null=True, blank=True),
        ),
    ]
