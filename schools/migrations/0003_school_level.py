# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0002_auto_20141010_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='level',
            field=models.CharField(default='unset', max_length=20, choices=[(b'elementary', b'Elementary'), (b'middle', b'Middle'), (b'secondary', b'Secondary'), (b'high', b'High')]),
            preserve_default=False,
        ),
    ]
