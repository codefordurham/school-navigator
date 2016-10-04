# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0022_school_principal_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolprofile',
            name='submitted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
