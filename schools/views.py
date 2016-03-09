from schools import forms as schools_forms
from django.shortcuts import render

def survey_form(request, hash):
    form = schools_forms.SchoolProfileForm()
    return render(request, 'survey_form.html', {'form': form})
