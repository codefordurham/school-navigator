# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0031_auto_20160418_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolprofile',
            name='extended_care_offered',
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='after_care_offered',
            field=models.NullBooleanField(help_text=' Do you provide after care?'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='before_care_offered',
            field=models.NullBooleanField(help_text=' Do you provide before care?'),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='lottery_deadline',
            field=models.DateTimeField(null=True, help_text='If your school has a lottery, what is the deadline for applying for the 2016-2017 school year?', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='other_academic',
            field=models.TextField(null=True, blank=True, help_text="Please describe any unique offerings, staff and additional resources that relate to your school's academic theme.", verbose_name='Academic theme'),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='principal_bio',
            field=models.TextField(null=True, help_text='Please provide a brief bio for the principal.', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='service_leadership',
            field=models.TextField(null=True, blank=True, help_text='Please describe your service & leadership extracurricular offerings.', verbose_name='Service & leadership'),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='survey_feedback',
            field=models.TextField(null=True, help_text='Thank you for taking the time to complete this survey!  Please let us know if you have any feedback on the process or on specific questions so we can improve next year.', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='theme',
            field=models.TextField(null=True, help_text='If your school has a particular theme or focus area, please enter the appropriate theme.  Typically one from the following list will apply: Math & Science, Arts, Language, College Ready, Montessori, Project-Based, Vocational Training, or Not Applicable - our school is for students of all backgrounds and interests.', blank=True),
        ),
    ]
