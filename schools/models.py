from django.contrib.gis.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils import timezone

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
    principal_email = models.CharField(max_length=100, null=True, blank=True,
                help_text='Email of Principal (may also reach Superintendent)'
    )

    type = models.CharField(choices=SCHOOL_TYPES, max_length=20)
    year_round = models.BooleanField(default=False)

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

        profile.submitted_at = None
        profile.created_at = None
        profile.save()
        return profile

    def profile(self):
        return self.schoolprofile_set.order_by('-created_at').first()

    def get_absolute_url(self):
        return '/#/school/{0}/'.format(self.pk)

    # Override default manager for gis
    objects = models.GeoManager()

    def __str__(self):
        return self.name

GRADE_LEVELS = (
    (-2, '3 year old prekindergarten'),
    (-1, '4 year old prekindergarten'),
    (0, 'Kindergarten'),
    (1, '1st grade'),
    (2, '2nd grade'),
    (3, '3rd grade'),
    (4, '4th grade'),
    (5, '5th grade'),
    (6, '6th grade'),
    (7, '7th grade'),
    (8, '8th grade'),
    (9, '9th grade'),
    (10, '10th grade'),
    (11, '11th grade'),
    (12, '12th grade'),
)

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

TRANSPORTATION = (
    ('all', 'Transportation is available for all students.'),
    ('some', 'Transportation is available for some students.'),
    ('none', 'We do not provide transportation for students.'),
)

class SchoolProfile(models.Model):
    school = models.ForeignKey('School')
    state_id = models.CharField(max_length=6, blank=True, null=True)

    level = models.CharField(choices=SCHOOL_LEVELS, max_length=20)
    school_hours = models.TextField(null=True, blank=True)
    grade_min = models.IntegerField(choices=GRADE_LEVELS, default=-2)
    grade_max = models.IntegerField(choices=GRADE_LEVELS, default=-2)
    website_url = models.CharField(max_length=500, blank=True, null=True)
    photo = models.ImageField(upload_to="school_photos/",null=True, blank=True)
    phone_number = models.TextField(null=True, blank=True,
            help_text='Please enter phone number in the format (919) XXX-XXXX.')
    year_opened = models.IntegerField(null=True, blank=True,
            help_text='In what year was your school opened?')
    speciality_type = models.TextField(null=True, blank=True)  # Is this still needed?  FIXME
    theme = models.TextField(null=True, blank=True,
            help_text='If your school has a particular theme or focus area, '
                'please enter the appropriate theme.  Typically one from the following list will apply: '
                'Math & Science, '
                'Arts, '
                'Language, '
                'College Ready, '
                'Montessori, '
                'Project-Based, '
                'Vocational Training, '
                'or Not Applicable - our school is for students of all backgrounds and interests.'
    )
    uniform_required = models.NullBooleanField(
            help_text='Does your school have a uniform for students?'
    )
    mission_statement = models.TextField(null=True, blank=True,
            help_text='What is your school’s mission statement?'
    )

    # About
    points_of_pride1 = models.TextField(null=True, blank=True,
            help_text='Please share three unique and specific Points of Pride about your school that families would want to know.',
            verbose_name='Point of Pride #1',
    )
    points_of_pride2 = models.TextField(null=True, blank=True,
            verbose_name='Point of Pride #2',
    )
    points_of_pride3 = models.TextField(null=True, blank=True,
            verbose_name='Point of Pride #3',
    )

    # School Services
    transportation = models.CharField(choices=TRANSPORTATION, max_length=4, blank=True,
            help_text='Do you provide transportation for students?'
    )
    transportation_explanation = models.TextField(null=True, blank=True,
            help_text='If you provide transportation, please describe how it is provided and for whom '
            '(I.E. one pick-up per neighborhood hub, city bus tickets provided to students)'
    )
    breakfast_served = models.CharField(max_length=4, choices=BREAKFAST, blank=True, null=True,
            help_text='Select the option that best describes your breakfast service.'
    )
    breakfast_explanation = models.TextField(null=True, blank=True,
            help_text='Please share any additional information that parents would like to know about your breakfast program.'
    )
    breakfast_free_and_reduced = models.NullBooleanField(
            help_text='Do you participate in the National Free and Reduced Breakfast Program?'
    )
    lunch_served = models.CharField(max_length=4, choices=LUNCH, blank=True, null=True,
            help_text='Select the option that best describes your lunch service.'
    )
    lunch_explanation = models.TextField(null=True, blank=True,
            help_text='Please share any additional information that parents would like to know about your lunch program.'
    )
    lunch_free_and_reduced = models.NullBooleanField(
            help_text='Do you participate in the National Free and Reduced Lunch Program?'
    )
    before_care_offered = models.NullBooleanField(
            help_text=' Do you provide before care?'
    )
    after_care_offered = models.NullBooleanField(
            help_text=' Do you provide after care?'
    )
    extended_care_cost = models.TextField(null=True, blank=True,
            help_text='What is the fee for before and/or after care?'
    )
    extended_care_financial_assistance = models.TextField(null=True, blank=True,
            help_text='Please describe any financial assistance available for before/after care.'
    )
    before_care_hours = models.TextField(null=True, blank=True,
            help_text='If you provide before care, please enter in the hours for care.'
    )
    after_care_hours = models.TextField(null=True, blank=True,
            help_text='If you provide after care, please enter in the hours for care.'
    )
    # Admissions Info
    admissions_policy_type = models.TextField(null=True, blank=True,
            help_text= 'Please write 1-2 sentences summarizing your admission policy.  Typically one of the following apply: '
            'Admission is guaranteed for all students who live in the designated zone for this school; '
            'Admission is guaranteed for students who live in the walk zone.  The remaining spots are filled through an open lottery; '
            'Admission is determined through an open lottery system.'
    )
    # FIXME make lottery_priority_X not a choice field??
    lottery_priority_1 = models.CharField(max_length=250, blank=True, null=True,
            help_text='If you have an admissions lottery, please list any groups (one group per box) that are given priority over the general applicant pool in the lottery (e.g. students in the walk zone, siblings of enrolled students, children of staff)'
    )
    lottery_priority_2 = models.CharField(max_length=250, blank=True, null=True)
    lottery_priority_3 = models.CharField(max_length=250, blank=True, null=True)
    lottery_priority_4 = models.CharField(max_length=250, blank=True, null=True)
    lottery_priority_5 = models.CharField(max_length=250, blank=True, null=True)
    lottery_deadline = models.DateTimeField(null=True, blank=True,
            help_text='If your school has a lottery, what is the deadline for applying for the 2017-2018 school year?  Use YYYY-MM-DD (like 2017-05-31) format.'
    )
    # lottery_acceptance_rate  FIXME
    learn_more_link = models.TextField(null=True, blank=True,
            help_text="Please provide a link where parents can learn more about your school’s admission process and apply."
    )
    feeder_school_info = models.TextField(null=True, blank=True,
            help_text="Do students graduating from your school have guaranteed enrollment or priority status in the lottery for another school?  If yes, please explain.  If not, please leave blank."
    )
    # Leadership & Teacher Info
    principal_name = models.TextField(null=True, blank=True,
            help_text='Name of Principal'
    )
    principal_bio = models.TextField(null=True, blank=True,
            help_text='Please provide a brief bio for the principal.'
    )
    principal_start_year = models.IntegerField(null=True, blank=True,
            help_text='Year that current principal began at this school:'
    )

    # Targeted Academic Offerings
    english_language_learner = models.TextField(null=True, blank=True,
            help_text='Please describe the offerings, staff and additional resources that you have for English Language Learners.'
    )
    special_education = models.TextField(null=True, blank=True,
            help_text='Please describe the offerings, staff and additional resources that you have for Exceptional Children.'
    )
    gifted_education = models.TextField(null=True, blank=True,
            help_text='Please describe the offerings, staff and additional resources that you have for the Academically & Intellectually Gifted.'
    )
    other_academic = models.TextField(null=True, blank=True,
            help_text="Please describe any unique offerings, staff and additional resources that relate to your school's academic theme.",
            verbose_name='Academic theme',
    )

    # Extracurricular
    academic = models.TextField(null=True, blank=True,
            help_text='Please describe your academic extracurricular offerings.'
    )
    arts = models.TextField(null=True, blank=True,
            help_text='Please describe your arts extracurricular offerings.'
    )
    sports = models.TextField(null=True, blank=True,
            help_text='Please describe your sports extracurricular offerings.'
    )
    service_leadership = models.TextField(null=True, blank=True,
            help_text='Please describe your service & leadership extracurricular offerings.',
            verbose_name='Service & leadership',
    )
    other = models.TextField(null=True, blank=True,
            help_text='Please describe your other extracurricular offerings.'
    )

    # Parent Involvement
    pta = models.NullBooleanField(
            help_text='Do you have a Parent Teacher Association or Parent Teacher Organization?',
            verbose_name='PTA/PTO',
    )
    pta_website = models.TextField(null=True, blank=True,
            help_text='If yes, please share the website or social media page for the PTA.',
            verbose_name='PTA website',
    )
    parental_involvement_notes = models.TextField(null=True, blank=True,
            help_text='Please provide any other information on parental involvement you would like parents to know.'
    )  # FIXME delete?

    # Survey Feedback
    survey_feedback = models.TextField(null=True, blank=True,
            help_text='Thank you for taking the time to complete this survey!  Please let us know if you have any feedback on the process or on specific questions so we can improve next year.'
    )

    submitted_at = models.DateTimeField(null=True, blank=True, default=None)
    created_at = models.DateTimeField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        super(SchoolProfile, self).save(force_insert=force_insert, force_update=force_update,
                                        using=using, update_fields=update_fields)
    def due_date(self):
        first_survey_due_date = datetime.date(2016, 7, 29)
        if datetime.date.today() < datetime.date(2016, 6, 30):
            return first_survey_due_date
        return (self.created_at + datetime.timedelta(30)).date()

    def overdue(self):
        tomorrow = (timezone.now() + datetime.timedelta(days=1)).date()
        return self.due_date() < tomorrow

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
        return reverse('school-survey-form', kwargs={'hash': self.url()})

    def __str__(self):
        return '{:s}'.format(self.school.name)


class Reflexions(models.Model):
    content = models.TextField(blank=True)
    school = models.ForeignKey(School)
