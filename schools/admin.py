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

        school_profile = school.new_profile()
        school_profile.save()
        school_profile_url = request.build_absolute_uri(school_profile.get_absolute_url())

        context = {
            'principal_name': 'principal_name',
            'due_date': school_profile.due_date(),
            'school_profile_url': school_profile_url,
        }
        body = render_to_string('survey_email.txt', context)

        EmailMessage(subject, body, to=to, from_email=from_email).send()


class SchoolAdmin(LeafletGeoAdmin):
    list_display = ('name', 'photo', 'type')
    ordering = ('name',)
    list_filter = ('type', )
    actions = [send_survey]

admin.site.register(School, SchoolAdmin)
admin.site.disable_action('delete_selected')
