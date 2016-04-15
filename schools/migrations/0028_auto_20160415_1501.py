# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0027_auto_20160415_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolprofile',
            name='academic',
            field=models.TextField(null=True, help_text='Please describe your academic extracurricular offerings.', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='admissions_policy_type',
            field=models.TextField(null=True, help_text='Please write 1-2 sentences summarizing your admission policy.  Typically one of the following apply: Admission is guaranteed for all students who live in the designated zone for this school; Admission is guaranteed for students who live in the walk zone.  The remaining spots are filled through an open lottery; Admission is determined through an open lottery system.', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='after_care_hours',
            field=models.TextField(null=True, help_text='If you provide after care, please enter in the hours for care.', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='arts',
            field=models.TextField(null=True, help_text='Please describe your arts extracurricular offerings.', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='before_care_hours',
            field=models.TextField(null=True, help_text='If you provide before care, please enter in the hours for care.', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='breakfast_explanation',
            field=models.TextField(null=True, help_text='Please share any additional information that parents would like to know about your breakfast program.', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='breakfast_free_and_reduced',
            field=models.NullBooleanField(help_text='Do you participate in the National Free and Reduced Breakfast Program?'),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='breakfast_served',
            field=models.CharField(null=True, blank=True, max_length=4, help_text='Select the option that best describes your breakfast service.', choices=[('all', 'Breakfast is available for all students.'), ('some', 'Breakfast is available for some students.'), ('none', 'We do not provide breakfast for students')]),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='english_langaue_learner',
            field=models.TextField(null=True, help_text='Please describe the offerings, staff and additional resources that you have for English Language Learners.', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='extended_care_cost',
            field=models.TextField(null=True, help_text='What is the fee for before and/or after care?', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='extended_care_fiancial_assistance',
            field=models.TextField(null=True, help_text='Please describe any financial assistance available for before/after care.', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='extended_care_offered',
            field=models.NullBooleanField(help_text=' Do you provide before or after care?'),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='gifted_education',
            field=models.TextField(null=True, help_text='Please describe the offerings, staff and additional resources that you have for the Academically & Intellectually Gifted.', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='learn_more_link',
            field=models.TextField(null=True, help_text='Please provide a link where parents can learn more about your school’s admission process and apply.', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='lottery_deadline',
            field=models.DateTimeField(null=True, help_text='If your school has a lottery, what is the deadline for applying?', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='lottery_priority_1',
            field=models.CharField(choices=[('a', 'Walk zone (guaranteed admission)'), ('b', 'Siblings of enrolled students'), ('c', 'Children of staff'), ('d', 'General applicant pool')], blank=True, max_length=20, help_text='If you have an admissions lottery, please list any groups (one group per box) that are given priority over the general applicant pool in the lottery (e.g. students in the walk zone, siblings of enrolled students, children of staff)'),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='lunch_explanation',
            field=models.TextField(null=True, help_text='Please share any additional information that parents would like to know about your lunch program.', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='lunch_free_and_reduced',
            field=models.NullBooleanField(help_text='Do you participate in the National Free and Reduced Lunch Program?'),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='lunch_served',
            field=models.CharField(null=True, blank=True, max_length=4, help_text='Select the option that best describes your lunch service.', choices=[('all', 'Lunch is available for all students.'), ('some', 'Lunch is available for some students.'), ('none', 'We do not provide lunch for students')]),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='mission_statement',
            field=models.TextField(null=True, help_text='What is your school’s mission statement?', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='other',
            field=models.TextField(null=True, help_text='Please describe your other extracurricular offerings.', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='points_of_pride1',
            field=models.TextField(null=True, help_text='Please share three unique and specific Points of Pride about your school that families would want to know.', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='principal_bio',
            field=models.TextField(null=True, help_text='Please provide a brief bio for the pricipal.', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='principal_name',
            field=models.TextField(null=True, help_text='Name of Principal', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='principal_start_year',
            field=models.IntegerField(null=True, help_text='Year that current principal began at this school:', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='pta',
            field=models.NullBooleanField(help_text='Do you have a parent teacher association?'),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='pta_website',
            field=models.TextField(null=True, help_text='If yes, please share the website or social media page for the PTA.', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='service_leadership',
            field=models.TextField(null=True, help_text='Please describe your service & leadership extracurricular offerings.', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='special_education',
            field=models.TextField(null=True, help_text='Please describe the offerings, staff and additional resources that you have for Exceptional Children.', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='sports',
            field=models.TextField(null=True, help_text='Please describe your sports extracurricular offerings.', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='theme',
            field=models.TextField(null=True, help_text='If your school has a particular theme or focus area, please wnter the appropriate theme from the following list: Math & Science, Arts, Language, College Ready, Montessori, Project-Based, Vocational Training, Not Applicable - our school is for students of all backgrounds and interests, or Other [write in answer] ', blank=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='transportation',
            field=models.CharField(choices=[('all', 'Transportation is available for all students.'), ('some', 'Transportation is available for some students.'), ('none', 'We do not provide transportation for students.')], blank=True, max_length=4, help_text='Do you provide transportation for students?'),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='uniform_required',
            field=models.NullBooleanField(help_text='Does your school have a uniform for students?'),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='year_opened',
            field=models.IntegerField(null=True, help_text='In what year was your school opened?'),
        ),
    ]
