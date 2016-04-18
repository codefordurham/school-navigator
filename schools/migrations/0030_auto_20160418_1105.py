# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0029_auto_20160418_1048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schoolprofile',
            old_name='english_langaue_learner',
            new_name='english_language_learner',
        ),
        migrations.RenameField(
            model_name='schoolprofile',
            old_name='extended_care_fiancial_assistance',
            new_name='extended_care_financial_assistance',
        ),
        migrations.RenameField(
            model_name='schoolprofile',
            old_name='tranportation_explanation',
            new_name='transportation_explanation',
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='other_academic',
            field=models.TextField(null=True, help_text='Please describe any other offerings, staff and additional resources that you provide.', blank=True),
        ),
    ]
