import requests

from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point, Polygon
import schools.models as schools_models

def query_api(api_endpoint_id):
    api_base  = 'http://gisweb2.ci.durham.nc.us/arcgis/rest/services/DurhamMaps/DPS_Schools/MapServer'
    api_get_params = {
            'outSR':'4326', #output spatial reference
            'where': '1=1', #grab all records
            'outFields' : '*', #all fields
            'f' : 'pjson'   #json file type
    }
    url = "%s/%s/query" % (api_base, api_endpoint_id)
    doc = requests.get(url, params=api_get_params)
    return doc.json()['features']

class Command(BaseCommand):
    help = 'Load up the data from GeoJSON into the models'

    def get_school(self, name, schools):
        if schools.has_key(name):
            return schools[name]
        else:
            school, created = schools_models.School.objects.get_or_create(name=name)
            return school

    def load_school_points(self, schools={}):
        school_point_id = 0
        for school in query_api(school_point_id):
            name = school['attributes']['School'].strip()
            s = self.get_school(name, schools)
            s.location = Point(
                    float(school['geometry']['x']),
                    float(school['geometry']['y'])
                )
            s.address = school['attributes']['ADDRESS'].strip()
            schools[name] = s
        return schools


    def load_districts(self, schools={}):
        #maps external API endpoint IDs to internal model choices
        school_level_mapping = [
            ('1', 'middle'),
            ('2', 'high'),
            ('3', 'elementary')
        ]
        school_grade_mapping = {
            'elementary' : (0, 4),
            'middle': (5, 8),
            'high': (9, 12),
        }

        for api_id, level in school_level_mapping:
            for district_json in query_api(api_id):
                name = district_json['attributes']['DISTRICT'].strip()
                s = self.get_school(name, schools)
                s.district = Polygon(district_json['geometry']['rings'][0])
                s.type = 'neighborhood'
                s.level = level
                s.grade_min, s.grade_max = school_grade_mapping[level]
                schools[name] = s
        return schools

    def load_zones(self, schools={}):
        school_walkzone_id = 6
        for school in query_api(school_walkzone_id):
            name = school['attributes']['NAME'].strip()
            s = self.get_school(name, schools)
            s = schools_models.School.objects.get(name=name)
            s.type = 'magnet'
            zone = Polygon(school['geometry']['rings'][0])
            zone_type = school['attributes']['TYPE_']
            if zone_type == "Walk Zone":
                s.walk_zone = zone
            if zone_type == "Choice Zone":
                s.choice_zone = zone
            if zone_type == "Priority":
                s.priority_zone = zone
            schools[name] = s
        return schools


    def handle(self, *args, **options):
        schools = {}
        schools = self.load_school_points(schools)
        schools = self.load_districts(schools)
        schools = self.load_zones(schools)
        for name in schools.keys():
            schools[name].save()
