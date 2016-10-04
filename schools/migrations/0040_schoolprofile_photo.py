# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0039_schoolprofile_state_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolprofile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='school_photos/', null=True),
        ),
    ]
