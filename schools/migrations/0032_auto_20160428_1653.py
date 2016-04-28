# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0031_auto_20160418_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolprofile',
            name='pta',
            field=models.NullBooleanField(verbose_name='PTA/PTO', help_text='Do you have a Parent Teacher Association or Parent Teacher Organization?'),
        ),
    ]
