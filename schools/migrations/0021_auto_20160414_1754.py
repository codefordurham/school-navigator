# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0020_auto_20160322_1955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schoolprofile',
            old_name='points_of_pride',
            new_name='points_of_pride1',
        ),
        migrations.RemoveField(
            model_name='schoolprofile',
            name='courses_offered',
        ),
        migrations.RemoveField(
            model_name='schoolprofile',
            name='extended_care_end',
        ),
        migrations.RemoveField(
            model_name='schoolprofile',
            name='extended_care_start',
        ),
        migrations.RemoveField(
            model_name='schoolprofile',
            name='extracurriculars',
        ),
        migrations.RemoveField(
            model_name='schoolprofile',
            name='parental_involvement',
        ),
        migrations.RemoveField(
            model_name='schoolprofile',
            name='total_enrollment',
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='academic',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='admissions_policy_type',
            field=models.TextField(help_text='Develop statements for neighborhood zone, YR zone, pure lottery, etc.', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='after_care_hours',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='arts',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='before_care_hours',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='breakfast_explanation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='breakfast_free_and_reduced',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='english_langaue_learner',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='extended_care_cost',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='extended_care_fiancial_assistance',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='extended_care_offered',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='learn_more_link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='lottery_deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='lottery_priority_1',
            field=models.CharField(blank=True, choices=[('a', 'Walk zone (guaranteed admission)'), ('b', 'Siblings of enrolled students'), ('c', 'Children of staff'), ('d', 'General applicant pool')], max_length=20),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='lottery_priority_2',
            field=models.CharField(blank=True, choices=[('a', 'Walk zone (guaranteed admission)'), ('b', 'Siblings of enrolled students'), ('c', 'Children of staff'), ('d', 'General applicant pool')], max_length=20),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='lottery_priority_3',
            field=models.CharField(blank=True, choices=[('a', 'Walk zone (guaranteed admission)'), ('b', 'Siblings of enrolled students'), ('c', 'Children of staff'), ('d', 'General applicant pool')], max_length=20),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='lottery_priority_4',
            field=models.CharField(blank=True, choices=[('a', 'Walk zone (guaranteed admission)'), ('b', 'Siblings of enrolled students'), ('c', 'Children of staff'), ('d', 'General applicant pool')], max_length=20),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='lottery_priority_5',
            field=models.CharField(blank=True, choices=[('a', 'Walk zone (guaranteed admission)'), ('b', 'Siblings of enrolled students'), ('c', 'Children of staff'), ('d', 'General applicant pool')], max_length=20),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='lunch_explanation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='lunch_free_and_reduced',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='other',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='parental_involvement_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='points_of_pride2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='points_of_pride3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='pta',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='pta_website',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='service_leadership',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='sports',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='theme',
            field=models.TextField(help_text='Please Enter: STEM (Science, Technology, Engineering, Math), Arts, Language, Humanities, College Ready, Montessori, Project-Based, Vocational Training, or write in answer', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='tranportation_explanation',
            field=models.TextField(help_text='If you provide transportation, please describe how it is provided and for whom (I.E. one pick-up per neighborhood hub, city bus tickets provided to students)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='transportation',
            field=models.CharField(blank=True, choices=[('all', 'Transportation is available for all students.'), ('some', 'Transportation is available for some students.'), ('none', 'We do not provide transportation for students.')], max_length=4),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='uniform_required',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='year_opened',
            field=models.IntegerField(help_text='Please use 4 digit years', null=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='breakfast_served',
            field=models.CharField(null=True, blank=True, choices=[('all', 'Breakfast is available for all students.'), ('some', 'Breakfast is available for some students.'), ('none', 'We do not provide breakfast for students')], max_length=4),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='gifted_education',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='lunch_served',
            field=models.CharField(null=True, blank=True, choices=[('all', 'Lunch is available for all students.'), ('some', 'Lunch is available for some students.'), ('none', 'We do not provide lunch for students')], max_length=4),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='phone_number',
            field=models.TextField(help_text='Please enter phone number in the format (919) XXX-XXXX.', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='principal_start_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='special_education',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='website_url',
            field=models.CharField(blank=True, null=True, max_length=500),
        ),
    ]
