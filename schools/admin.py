from django import forms
from django.conf import settings
from django.contrib import admin
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

from leaflet.admin import LeafletGeoAdmin

from .models import School, SchoolProfile

SN_EMAIL = 'schoolnavigatorteam@gmail.com'
CC_DPS_EMAIL = ['William.Sudderth-III@dpsnc.net', SN_EMAIL]
CC_CHARTER_EMAIL = [SN_EMAIL]

def send_email(school, request):
    subject = 'Durham School Navigator Survey Request: {:s}'.format(school.name)
    if school.principal_email is None:
        school.principal_email = ''
    to = [school.principal_email]
    from_email = settings.FROM_EMAIL

    school_profile = school.profile()
    school_profile_url = request.build_absolute_uri(school_profile.get_absolute_url())

    if school.type == 'charter':
        email_template = 'survey_email_charter.txt'
        cc = CC_CHARTER_EMAIL
    else:
        email_template = 'survey_email_dps.txt'
        cc = CC_DPS_EMAIL

    context = {
        'school': school,
        'school_profile': school_profile,
        'principal_name': school_profile.principal_name,
        'school_profile_url': school_profile_url,
    }
    body = render_to_string(email_template, context)

    EmailMessage(subject, body, to=to, from_email=from_email, cc=cc).send()

def send_survey(modeladmin, request, queryset):
    for school in queryset:
        school.new_profile()
        send_email(school, request)
    message = "Tried to send {0!s} survey(s)".format(queryset.count())
    messages.info(request, message)

def resend_survey(modeladmin, request, queryset):
    email_count = 0
    for school in queryset:
        if not school.profile().overdue():
            send_email(school, request)
            email_count += 1
    message = "Tried to re-send {0!s} survey(s)".format(email_count)
    messages.info(request, message)


class SchoolForm(forms.ModelForm):
    principal_name = forms.CharField(required=False)

    class Meta:
        model = School
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SchoolForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.profile():
            self.initial['principal_name'] = self.instance.profile().principal_name

    def save(self, commit=False, *args, **kwargs):
        principal_name = self.cleaned_data.pop('principal_name')
        if self.instance:
            profile = self.instance.profile()
            if profile:
                profile.principal_name = principal_name
                profile.save()
        return super(SchoolForm, self).save(commit=commit, *args, **kwargs)


class SchoolAdmin(LeafletGeoAdmin):
    form = SchoolForm
    list_display = ('name', 'principal_email', 'principal_name', 'profile_status', 'profile', 'photo', 'type')
    list_editable = ('principal_email',)
    ordering = ('name',)
    list_filter = ('type', )
    actions = [send_survey, resend_survey]
    fields = ('name', 'short_name', 'address', 'zip_code', 'active', 'photo',
              'principal_email', 'principal_name', 'type', 'year_round', 'location',
              'district', 'walk_zone', 'choice_zone', 'priority_zone', 'year_round_zone',
              'traditional_option_zone')

    def photo(self, obj):
        return getattr(obj.profile(), 'photo', '')

    def get_changelist_form(self, request, **kwargs):
            return SchoolForm

    def principal_name(self, obj):
        return getattr(obj.profile(), 'principal_name', '')

    def profile_status(self, obj):
        profile = obj.profile()
        if profile:
            if profile.overdue():
                return 'Over due'
            return 'Submitted'
        return ''

    def profile(self, obj):
        profile = obj.profile()
        if profile:
            url = reverse('admin:schools_schoolprofile_change', args=(profile.id,))
            return '<a href={url}><i class="fa fa-link" aria-hidden="true"></i></a>'.format(url=url)
        return ''
    profile.allow_tags = True

    class Media:
        js = ('https://use.fontawesome.com/c8bb83e4c1.js',)


admin.site.register(School, SchoolAdmin)
admin.site.disable_action('delete_selected')

class SchoolProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'due_date', 'created_at', 'submitted_at')
    ordering = ('created_at', )
admin.site.register(SchoolProfile, SchoolProfileAdmin)
