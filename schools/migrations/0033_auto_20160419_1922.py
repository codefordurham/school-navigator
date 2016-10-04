# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0032_auto_20160419_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolprofile',
            name='lottery_priority_1',
            field=models.CharField(max_length=250, null=True, blank=True, help_text='If you have an admissions lottery, please list any groups (one group per box) that are given priority over the general applicant pool in the lottery (e.g. students in the walk zone, siblings of enrolled students, children of staff)'),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='lottery_priority_2',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='lottery_priority_3',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='lottery_priority_4',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='lottery_priority_5',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
    ]
