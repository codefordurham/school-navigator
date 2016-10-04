# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.contrib.gis.geos import MultiPolygon
import django.contrib.gis.db.models.fields


def convert_polygons(apps, schema_editor):
    School = apps.get_model("schools", "School")
    for school in School.objects.all():
        if school.district:
            school.district = MultiPolygon(school.district)
        if school.walk_zone:
            school.walk_zone = MultiPolygon(school.walk_zone)
        if school.choice_zone:
            school.choice_zone = MultiPolygon(school.choice_zone)
        if school.priority_zone:
            school.priority_zone = MultiPolygon(school.priority_zone)
        if school.year_round_zone:
            school.year_round_zone = MultiPolygon(school.year_round_zone)
        school.save()


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0011_school_year_round_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='choice_zone',
            field=django.contrib.gis.db.models.fields.GeometryField(srid=4326, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='district',
            field=django.contrib.gis.db.models.fields.GeometryField(srid=4326, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='priority_zone',
            field=django.contrib.gis.db.models.fields.GeometryField(srid=4326, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='walk_zone',
            field=django.contrib.gis.db.models.fields.GeometryField(srid=4326, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='year_round_zone',
            field=django.contrib.gis.db.models.fields.GeometryField(srid=4326, blank=True, null=True),
        ),
        migrations.RunPython(convert_polygons),
        migrations.AlterField(
            model_name='school',
            name='choice_zone',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='district',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='priority_zone',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='walk_zone',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='year_round_zone',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, blank=True, null=True),
        ),
    ]


# from schools.models import School
# from django.contrib.gis.geos import Polygon, MultiPolygon
# school = School.objects.filter(type="neighborhood")[0]
# school.district
