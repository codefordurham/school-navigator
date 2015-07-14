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

def query_api2(api_endpoint_id, api_section):
    api_base = 'http://gisweb2.ci.durham.nc.us/arcgis/rest/services/DurhamMaps/{api_section}/MapServer'.format(api_section=api_section)
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
        if name in schools:
            return schools[name]
        else:
            defaults = {
                'location': Point(0,0),
                'grade_max': -100,
                'grade_min': -100,
            }
            school, created = schools_models.School.objects.get_or_create(name=name, defaults=defaults)
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
            if school['attributes']['MAGNET'] == 'Magnet':
                s.type = 'magnet'
            if school['attributes']['YEARROUND'] == "Year-Round":
                s.year_round = True
            s.level = school['attributes']['TYPE_'].lower()
            s.website_url = school['attributes']['WEBSITE']
            s.grade_min = school['attributes']['Low_Grade']
            s.grade_max = school['attributes']['Top_Grade']
            schools[name] = s
        return schools


    def load_districts(self, schools={}):
        for api_id in (1, 2, 3):
            for district_json in query_api(api_id):
                name = district_json['attributes']['DISTRICT'].strip()
                s = self.get_school(name, schools)
                s.district = Polygon(district_json['geometry']['rings'][0])
                s.type = 'neighborhood'
                schools[name] = s
        return schools

    def load_zones(self, schools={}):
        school_walkzone_id = 6
        for school in query_api(school_walkzone_id):
            name = school['attributes']['NAME'].strip()
            s = self.get_school(name, schools)
            s.type = 'magnet'
            zone = Polygon(school['geometry']['rings'][0])
            zone_type = school['attributes']['TYPE_']
            if zone_type == "Walk Zone":
                s.walk_zone = zone
            if zone_type == "Choice Zone":
                s.choice_zone = zone
            if zone_type == "Priority Zone":
                s.priority_zone = zone
            schools[name] = s
        return schools

    def load_year_round_elementary(self, schools={}):
        api_end_point = 3
        api_section = 'DPS_ElementaryStudentAssignment'
        for school in query_api2(api_end_point, api_section):
            name = school['attributes']['YEARRND_ES'].strip()
            s = self.get_school(name, schools)
            s.type = 'magnet'
            s.year_round_zone = Polygon(school['geometry']['rings'][0])
            schools[name] = s
        return schools

    def load_year_round_middle(self, schools={}):
        api_end_point = 2
        api_section = 'DPS_MiddleSchoolStudentAssignment'
        for school in query_api2(api_end_point, api_section):
            name = school['attributes']['YEARRND_MS'].strip()
            s = self.get_school(name, schools)
            s.type = 'magnet'
            s.year_round_zone = Polygon(school['geometry']['rings'][0])
            schools[name] = s
        return schools

    def handle(self, *args, **options):
        schools = {}
        schools = self.load_school_points(schools)
        schools = self.load_districts(schools)
        schools = self.load_zones(schools)
        schools = self.load_year_round_elementary(schools)
        schools = self.load_year_round_middle(schools)
        for name in schools.keys():
            schools[name].save()
