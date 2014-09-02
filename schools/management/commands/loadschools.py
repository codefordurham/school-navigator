import requests
import json

from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import Point, Polygon, LinearRing
import schools.models as schools_models

class Command(BaseCommand):
    help = 'Load up the data from GeoJSON into the models'
    api_base  = 'http://gisweb2.ci.durham.nc.us/arcgis/rest/services/DurhamMaps/DPS_Schools/MapServer'
    api_get_params = {
            'outSR':'4326', #output spatial reference
            'where': '1=1', #grab all records
            'f' : 'pjson'   #json file type
    }

    def query_api(self, api_endpoint_id):
        url = "%s/%s/query" % (self.api_base, api_endpoint_id)
        doc = requests.get(url, params=self.api_get_params)
        return doc.json()['features']

    def load_school_points(self):
        school_point_id = 0
        d = self.query_api(school_point_id)
        for school in d:
            s = schools_models.School(name=school['attributes']['School'],
                    location=Point(
                        float(school['geometry']['x']),
                        float(school['geometry']['y'])))
            s.save()

    def load_districts(self):
        #maps external API endpoint IDs to internal model choices
        school_level_mapping = [
                ('1', schools_models.MID),
                ('2', schools_models.HIGH),
                ('3', schools_models.ELEM)
        ]
        for api_id, level in school_level_mapping:
            d = self.query_api(api_id)
            for district_json in d:
                name = district_json['attributes']['DISTRICT']
                school = schools_models.School.objects.get(name=name)
                school.district = Polygon(district_json['geometry']['rings'][0])
                school.level = level
                school.save()

    def load_walkzones(self):
        school_walkzone_id = 6
        d = self.query_api(school_walkzone_id)
        for school in d:
            name = school['attributes']['NAME']
            school = schools_models.School.objects.get(name=name)
            school.walk_zone = Polygon(d[1]['geometry']['rings'][0])
            school.magnet = True
            school.save()


    def handle(self, *args, **options):
        self.load_school_points()
        self.load_districts()
        self.load_walkzones()
