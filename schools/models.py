from django.contrib.gis.db import models
from django.conf import settings

from hashids import Hashids

import datetime

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
    active = models.BooleanField(default=False)
    photo = models.ImageField(null=True, blank=True)

    type = models.CharField(choices=SCHOOL_TYPES, max_length=20)

    location = models.PointField()
    district = models.MultiPolygonField(null=True, blank=True)

    # Zones per http://dpsncapplication.com/site327.php
    walk_zone = models.MultiPolygonField(null=True, blank=True)
    choice_zone = models.MultiPolygonField(null=True, blank=True)
    priority_zone = models.MultiPolygonField(null=True, blank=True)
    year_round_zone = models.MultiPolygonField(null=True, blank=True)
    traditional_option_zone = models.MultiPolygonField(null=True, blank=True)

    def new_profile(self):
        profile = self.profile()
        if profile:
            profile.pk = None
        else:
            profile = SchoolProfile.objects.create(school=self)
        return profile

    def profile(self):
        return self.schoolprofile_set.order_by('-created_at').first()

    # Override default manager for gis
    objects = models.GeoManager()

    def __str__(self):
        return self.name

BREAKFAST = (
    ('all', 'Breakfast is available for all students.'),
    ('some', 'Breakfast is available for some students.'),
    ('none', 'We do not provide breakfast for students'),
)

LUNCH = (
    ('all', 'Lunch is available for all students.'),
    ('some', 'Lunch is available for some students.'),
    ('none', 'We do not provide lunch for students'),
)

class SchoolProfile(models.Model):
    school = models.ForeignKey('School')

    level = models.CharField(choices=SCHOOL_LEVELS, max_length=20)
    year_round = models.BooleanField(default=False)
    school_hours = models.TextField(null=True, blank=True)
    grade_min = models.IntegerField()
    grade_max = models.IntegerField()
    website_url = models.CharField(max_length=500, blank=True)
    phone_number = models.TextField(null=True, blank=True) # validation??
    year_opened = models.IntegerField(blank=True) # make sure it is 4 digits
    speciality_type = models.TextField(null=True, blank=True)
    theme = models.TextField(null=True, blank=True) # want to have choices and a free response
                                                    # see cell F17 in sarah google docs
    uniform_required = models.NullBooleanField()
    mission_statement = models.TextField(null=True, blank=True)
    
    # About
    points_of_pride1 = models.TextField(null=True, blank=True)
    points_of_pride2 = models.TextField(null=True, blank=True)
    points_of_pride3 = models.TextField(null=True, blank=True)
    
    # School Services
    tranportation = models.TextField(null=True, blank=True) # want to have choices and a free response
                                                            # see cell F23
    tranportation_explanation(TextField, blank=True)
    breakfast_served = models.CharField(choices=BREAKFAST)
    breakfast_explanation = models.TextField(null=True, blank=True)
    breakfast_free_and_reduced = models.NullBooleanField()
    lunch_served = models.CharField(choices=LUNCH)
    lunch_explanation = models.TextField(null=True, blank=True)
    lunch_free_and_reduced = models.NullBooleanField()
    extended_care_offered = models.NullBooleanField()
    extended_care_cost = models.TextField(null=True, blank=True)
    extended_care_fiancial_assistance = models.TextField()
    before_care_hours = models.TextField(null=True, blank=True)
    after_care_hours = models.TextField(null=True, blank=True)

    # Admissions Info
    # FIXME

    # Leadership & Teacher Info
    principal_name = models.TextField(null=True, blank=True)
    principal_bio = models.TextField(null=True, blank=True)
    principal_start_year = models.IntegerField(null=True)

    # Targeted Academic Offerings
    english_langaue_learner = models.TextField(null=True, blank=True)
    special_education = models.TextField(null=True, blank=True)
    gifted_education = models.TextField(null=True, blank=True)
    # are there others? FIXME

    # Extracurricular
    academic = models.TextField(null=True, blank=True)
    arts = models.TextField(null=True, blank=True)
    sports = models.TextField(null=True, blank=True)
    service_leadership = models.TextField(null=True, blank=True)
    other = models.TextField(null=True, blank=True)

    # Parent Involvement
    pta = models.NullBooleanField()
    pta_website = models.TextField(null=True, blank=True)
    parental_involvement_notes = models.TextField(null=True, blank=True)

    submitted_at = models.DateTimeField(null=True, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def due_date(self):
        return self.created_at + datetime.timedelta(30)

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

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school-survey-form', kwargs={'hash': self.url()})

    def __str__(self):
        return '{:s}'.format(self.school.name)


class Reflexions(models.Model):
    content = models.TextField(blank=True)
    school = models.ForeignKey(School)
