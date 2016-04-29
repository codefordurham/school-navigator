# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0036_auto_20160428_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolprofile',
            name='lottery_deadline',
            field=models.DateTimeField(help_text='If your school has a lottery, what is the deadline for applying for the 2017-2018 school year?  Use YYYY-MM-DD (like 2017-05-31) format.', null=True, blank=True),
        ),
    ]
