import requests

from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point, Polygon
import schools.models as schools_models


class Command(BaseCommand):
    help = 'Load up the data from GeoJSON into the models'
    base_url = 'http://www.ncschoolreportcard.org/src/search.jsp'
    params = {
        "pYear":"2012-2013",
        "pList": "1",
        "pListVal": "320%3ADurham+Public+Schools+++++++++++++++++++&GO2=GO"
    }


    def handle(self, *args, **options):
        doc = requests.get(self.base_url, params=self.params)
        print doc

