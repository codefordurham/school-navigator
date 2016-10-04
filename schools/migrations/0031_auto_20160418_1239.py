# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0030_auto_20160418_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolprofile',
            name='grade_max',
            field=models.IntegerField(choices=[(-2, '3 year old prekindergarten'), (-1, '4 year old prekindergarten'), (0, 'Kindergarten'), (1, '1st grade'), (2, '2nd grade'), (3, '3rd grade'), (4, '4th grade'), (5, '5th grade'), (6, '6th grade'), (7, '7th grade'), (8, '8th grade'), (9, '9th grade'), (10, '10th grade'), (11, '11th grade'), (12, '12th grade')]),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='grade_min',
            field=models.IntegerField(choices=[(-2, '3 year old prekindergarten'), (-1, '4 year old prekindergarten'), (0, 'Kindergarten'), (1, '1st grade'), (2, '2nd grade'), (3, '3rd grade'), (4, '4th grade'), (5, '5th grade'), (6, '6th grade'), (7, '7th grade'), (8, '8th grade'), (9, '9th grade'), (10, '10th grade'), (11, '11th grade'), (12, '12th grade')]),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='parental_involvement_notes',
            field=models.TextField(blank=True, null=True, help_text='Please provide any other information on parental involvement you would like parents to know.'),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='points_of_pride1',
            field=models.TextField(blank=True, help_text='Please share three unique and specific Points of Pride about your school that families would want to know.', null=True, verbose_name='Point of Pride #1'),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='points_of_pride2',
            field=models.TextField(blank=True, null=True, verbose_name='Point of Pride #2'),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='points_of_pride3',
            field=models.TextField(blank=True, null=True, verbose_name='Point of Pride #3'),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='pta',
            field=models.NullBooleanField(help_text='Do you have a Parent Teacher Association?', verbose_name='PTA'),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='pta_website',
            field=models.TextField(blank=True, help_text='If yes, please share the website or social media page for the PTA.', null=True, verbose_name='PTA website'),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='theme',
            field=models.TextField(blank=True, null=True, help_text='If your school has a particular theme or focus area, please enter the appropriate theme from the following list: Math & Science, Arts, Language, College Ready, Montessori, Project-Based, Vocational Training, Not Applicable - our school is for students of all backgrounds and interests, or Other [write in answer] '),
        ),
    ]
