from django.contrib.gis.db import models

SCHOOL_LEVELS = (
    ('elementary', 'Elementary'),
    ('middle', 'Middle'),
    ('secondary', 'Secondary'),
    ('high', 'High')
)

SCHOOL_TYPES = (
    ('neighborhood', 'Neighborhood'),
    ('magnet', 'Magnet'),
    ('charter', 'Charter'),
    ('speciality', 'Specialty')
)


class School(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=5, blank=True)
    address = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=5, blank=True)
    website_url = models.CharField(max_length=500, blank=True)
    mission_statement = models.TextField(null=True, blank=True)
    school_hours = models.TextField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)

    level = models.CharField(choices=SCHOOL_LEVELS, max_length=20)
    type = models.CharField(choices=SCHOOL_TYPES, max_length=20)
    year_round = models.BooleanField(default=False)
    grade_min = models.IntegerField()
    grade_max = models.IntegerField()

    location = models.PointField()
    district = models.PolygonField(null=True, blank=True)

    # Zones per http://dpsncapplication.com/site327.php
    walk_zone = models.PolygonField(null=True, blank=True)
    choice_zone =  models.PolygonField(null=True, blank=True)
    priority_zone = models.PolygonField(null=True, blank=True)

    # Override default manager for gis
    objects = models.GeoManager()

    def __str__(self):
        return self.name
