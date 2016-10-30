# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0045_auto_20161018_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='teacher_satisfaction_survey',
            field=models.URLField(null=True),
        ),
    ]
