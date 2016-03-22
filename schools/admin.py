from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import admin
from django.template import Context
from django.template.loader import render_to_string, get_template

from leaflet.admin import LeafletGeoAdmin

from .models import School, SchoolProfile


def send_survey(modeladmin, request, queryset):
    for school in queryset:
        subject = 'Durham School Navigator Survey: {:s}'.format(school.name)
        to = ['principal_email']
        #to = [school.principal_email],
        from_email = settings.FROM_EMAIL

        school_profile = SchoolProfile.objects.create(school=school)
        school_profile_url = request.build_absolute_uri(school_profile.get_absolute_url())

        context = {
            'principal_name': 'principal_name',
            'due_date': 'due_date',
            'school_profile_url': school_profile_url,
        }
        body = render_to_string('survey_email.txt', context)

        EmailMessage(subject, body, to=to, from_email=from_email).send()


class SchoolAdmin(LeafletGeoAdmin):
    list_display = ('name', 'level', 'has_mission_statement', 'photo',
            'school_hours', 'type', 'year_round', 'grade_min', 'grade_max')
    ordering = ('name',)
    list_filter = ('year_round', 'level', 'type')
    actions = [send_survey]

    def has_mission_statement(self, obj):
        if obj.mission_statement:
            return True
        return False
    has_mission_statement.boolean = True

admin.site.register(School, SchoolAdmin)
