import csv
import sys

from django.core.management.base import BaseCommand
import schools.models as schools_models


class Command(BaseCommand):
    help = 'Get a CSV of survey feedback'

    def handle(self, *args, **options):
        headers = ['name', 'created_at', 'type', 'feedback']
        writer = csv.DictWriter(sys.stdout, fieldnames=headers)
        writer.writeheader()
        for profile in schools_models.SchoolProfile.objects.select_related('school').order_by('school__name','-created_at'):
            row = {
                'name': profile.school.name,
                'created_at': profile.created_at,
                'type': profile.school.type,
                'feedback': profile.survey_feedback,
            }
            writer.writerow(row)
