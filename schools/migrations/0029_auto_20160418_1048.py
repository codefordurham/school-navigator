# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0028_auto_20160415_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolprofile',
            name='other_academic',
            field=models.TextField(null=True, blank=True, help_text='Please describe the offerings, staff and additional resources that you have for the Academically & Intellectually Gifted.'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='survey_feedback',
            field=models.TextField(null=True, blank=True),
        ),
    ]
