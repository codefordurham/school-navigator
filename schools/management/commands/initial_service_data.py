import requests

from django.core.management.base import BaseCommand
import schools.models as schools_models


class Command(BaseCommand):
    help = 'Initial data for transportation, breakfast, and lunch.'

    def handle(self, *args, **options):
        profiles = schools_models.SchoolProfile.objects.all()
        profiles.filter(school__type='neighborhood').update(admissions_policy_type = 'Admission is guaranteed for all students who live in the designated zone for this school')

        for profile in profiles.exclude(school__type='charter'):
            profile.transportation = 'all'
            profile.breakfast_served = 'all'
            profile.lunch_served = 'all'
            profile.breakfast_free_and_reduced = True
            profile.lunch_free_and_reduced = True
            profile.save()
