# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def move_to_profile(apps, schema_editor):
    School = apps.get_model('schools', 'School')
    SchoolProfile = apps.get_model('schools', 'SchoolProfile')
    # create initial SchoolProfile from School and copy relevant fields (that
    # will be deleted in the next migration)
    for school in School.objects.all():
        school.schoolprofile_set.create(
            website_url=school.website_url,
            mission_statement=school.mission_statement,
            school_hours=school.school_hours,
            level=school.level,
            type=school.type,
            year_round=school.year_round,
            grade_min=school.grade_min,
            grade_max=school.grade_max,
        )



class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0018_auto_20160322_1904'),
    ]

    operations = [
        migrations.RunPython(move_to_profile),
    ]
