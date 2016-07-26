# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def move_to_profile(apps, schema_editor):
    School = apps.get_model('schools', 'School')
    SchoolProfile = apps.get_model('schools', 'SchoolProfile')
    # move existing photos to profile model
    for school in School.objects.all():
        profile = school.schoolprofile_set.order_by('-created_at').first()
        profile.photo = school.photo
        profile.save()


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0040_schoolprofile_photo'),
    ]

    operations = [
        migrations.RunPython(move_to_profile),
    ]
