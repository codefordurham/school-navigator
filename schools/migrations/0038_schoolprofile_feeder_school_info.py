# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0037_auto_20160428_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolprofile',
            name='feeder_school_info',
            field=models.TextField(null=True, help_text='Do students graduating from your school have guaranteed enrollment or priority status in the lottery for another school?  If yes, please explain.  If not, please leave blank.', blank=True),
        ),
    ]
