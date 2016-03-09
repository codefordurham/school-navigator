from datetime import datetime, timedelta

from schools import forms as schools_forms
from schools import models as schools_models

from django.shortcuts import render
from django.http import Http404

def survey_form(request, hash):
    try:
        pk = schools_models.SchoolProfile.decode_url(hash)
    except:
        raise Http404("Survey does not exist")
    profile = schools_models.SchoolProfile.objects.get(pk=pk)
    if profile.submitted_at and \
            profile.submitted_at > datetime.datetime.now() + timedelta(days=1):
        raise Http404("Survey Already Completed")
    form = schools_forms.SchoolProfileForm(instance=profile)
    return render(request, 'survey_form.html', {'survey_form': form})
