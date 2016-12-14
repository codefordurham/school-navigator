import requests

from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
import schools.models as schools_models


class Command(BaseCommand):
    help = 'Gets teacher satisfaction survey data'

    def handle(self, *args, **options):
        teacher_survey = self.get_teacher_survey('https://ncteachingconditions.org/results/report/427/133693')
        # print(teacher_survey.keys())
        # for school in schools_models.School.objects.all():
        #     teacher_survey = self.get_teacher_survey(school.satisfaction_survey_url)
        #     pass

    def get_teacher_survey(self, url):
        response = requests.get(url, verify=False)
        soup = BeautifulSoup(response.content, 'html.parser')
        data = {}
        for box in soup.findAll(True, {'class': ['non-breaking-box']}):
            school_data = {}
            district_data = {}
            title = box.find('h5').get_text()
            district_box = box.find(True, {'class': ['rowdistrict', 'responsebartierdata']})
            school_box = box.find(True, {'class': ['rowschool', 'responsebartierdata']})
            school_strongly_agree = school_box.find(True, {'data-original-title': 'Strongly agree'})
            school_agree = ''
            print(school_box)
            data[title] = {
                'district': district_box,
                'school': school_box,
            }
        return data
