# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def move_to_profile(apps, schema_editor):
    School = apps.get_model('schools', 'School')
    SchoolProfile = apps.get_model('schools', 'SchoolProfile')
    # create initial SchoolProfile from School and copy relevant fields (that
    # will be deleted in the next migration)
    for profile in SchoolProfile.objects.all():
        school = profile.school
        school.year_round = profile.year_round
        school.save()


def do_nothing(apps, schema_editor):
    School = apps.get_model('schools', 'School')
    SchoolProfile = apps.get_model('schools', 'SchoolProfile')
    # create initial SchoolProfile from School and copy relevant fields (that
    # will be deleted in the next migration)
    for school in School.objects.all():
        profile = school.profile
        if profile:
            profile.year_round = profile.year_round
            profile.save()


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0024_school_year_round'),
    ]

    operations = [
        migrations.RunPython(move_to_profile, do_nothing),
    ]
