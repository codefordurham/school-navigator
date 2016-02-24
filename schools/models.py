from django.contrib.gis.db import models

from hashids import Hashids
from django.conf import settings

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
    active = models.BooleanField(default=False)

    level = models.CharField(choices=SCHOOL_LEVELS, max_length=20)
    type = models.CharField(choices=SCHOOL_TYPES, max_length=20)
    year_round = models.BooleanField(default=False)
    grade_min = models.IntegerField()
    grade_max = models.IntegerField()

    location = models.PointField()
    district = models.MultiPolygonField(null=True, blank=True)

    # Zones per http://dpsncapplication.com/site327.php
    walk_zone = models.MultiPolygonField(null=True, blank=True)
    choice_zone = models.MultiPolygonField(null=True, blank=True)
    priority_zone = models.MultiPolygonField(null=True, blank=True)
    year_round_zone = models.MultiPolygonField(null=True, blank=True)
    traditional_option_zone = models.MultiPolygonField(null=True, blank=True)

    # Override default manager for gis
    objects = models.GeoManager()

    def __str__(self):
        return self.name

class SchoolProfile(models.Model):
    school = models.ForeignKey('School')

    # Pictures
    # - School.photo

    # School Data
    # - School.type
    # - School.level
    # - School.grade_min
    # - School.grade_max
    speciality_type = models.TextField(null=True, blank=True)
    phone_number = models.TextField(null=True, blank=True)
    # - School.website_url
    # - School.school_hours
    total_enrollment = models.IntegerField(null=True)
    breakfast_served = models.NullBooleanField()
    lunch_served = models.NullBooleanField()

    # About
    # - School.mission_statement
    points_of_pride = models.TextField(null=True, blank=True)

    # Admissions Info

    # Leadership & Teacher Info
    principal_name = models.TextField(null=True, blank=True)
    principal_bio = models.TextField(null=True, blank=True)
    principal_start_year = models.IntegerField(null=True)

    # Extracurriculars
    extracurriculars = models.TextField(null=True)

    # Course Offerings
    courses_offered = models.TextField(null=True)
    special_education = models.TextField(null=True)
    gifted_education = models.TextField(null=True)

    # Before & After Care
    extended_care_start = models.TimeField(null=True)
    extended_care_end = models.TimeField(null=True)

    # Parent Involvement
    parental_involvement = models.TextField(null=True)

    def url(self):
        hashids = Hashids(salt=settings.SECRET_KEY, min_length=10)
        return hashids.encode(self.id)

    @classmethod
    def decode_url(self, url):
        hashids = Hashids(salt=settings.SECRET_KEY, min_length=10)
        decoded = hashids.decode(url)
        if not decoded:
            raise Exception("Could not decode hashid to pk")
        return decoded[0]

    def __str__(self):
        return self.school.name + '-' + self.url()


class Reflexions(models.Model):
    content = models.TextField(blank=True)
    school = models.ForeignKey(School)
