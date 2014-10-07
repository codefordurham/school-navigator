import os
from json import dump
from optparse import make_option
import requests

from django.contrib.gis.geos import Point, Polygon
from django.core.management.base import BaseCommand

import schools.models as schools_models


DUMP_DIR = 'geojson'


class Command(BaseCommand):
    help = 'Load up the data from GeoJSON into the models'
    api_base = 'http://gisweb2.ci.durham.nc.us/arcgis/rest/services/DurhamMaps/DPS_Schools/MapServer'
    api_get_params = {
        'outSR': '4326',  # output spatial reference
        'where': '1=1',  # grab all records
        'f': 'pjson'  # json file type
    }
    option_list = BaseCommand.option_list + (make_option(
        '--download',
        action='store_true',
        dest='download',
        default=False,
        help='Download to files rather than loading into database.'),)

    def query_api(self, api_endpoint_id, download_only=False):
        url = "%s/%s/query" % (self.api_base, api_endpoint_id)
        doc = requests.get(url, params=self.api_get_params)
        if download_only:
            return doc.json()
        else:
            return doc.json()['features']

    def load_school_points(self, download_only):
        school_point_id = 0
        d = self.query_api(school_point_id, download_only)
        if download_only:
            filename = os.path.join(DUMP_DIR, 'schools.json')
            with open(filename, 'w') as school_file:
                dump(d, school_file, indent=4)
        else:
            for school in d:
                s = schools_models.School(name=school['attributes']['School'],
                                          location=Point(
                                              float(school['geometry']['x']),
                                              float(school['geometry']['y'])))
                s.save()

    def load_districts(self, download_only):
        # maps external API endpoint IDs to internal model choices
        school_level_mapping = [
            ('1', schools_models.MID),
            ('2', schools_models.HIGH),
            ('3', schools_models.ELEM)
        ]
        district_json_dump = {}
        for api_id, level in school_level_mapping:
            d = self.query_api(api_id, download_only)
            if download_only:
                district_json_dump[api_id] = d
            else:
                for district_json in d:
                    name = district_json['attributes']['DISTRICT']
                    school = schools_models.School.objects.get(name=name)
                    school.district = Polygon(district_json['geometry']['rings'][0])
                    school.level = level
                    school.save()
        if district_json_dump != {}:
            for api_id in district_json_dump.keys():
                filename = 'districts_%s.json' % api_id
                filename = os.path.join(DUMP_DIR, filename)
                with open(filename, 'w') as districts_file:
                    dump(district_json_dump[api_id], districts_file, indent=4)

    def load_walkzones(self, download_only):
        school_walkzone_id = 6
        d = self.query_api(school_walkzone_id, download_only)
        if download_only:
            filename = os.path.join(DUMP_DIR, 'walkzones.json')
            with open(filename, 'w') as walkzone_file:
                dump(d, walkzone_file, indent=4)
                walkzone_file.write('one')
        else:
            for school in d:
                name = school['attributes']['NAME']
                school = schools_models.School.objects.get(name=name)
                school.walk_zone = Polygon(d[1]['geometry']['rings'][0])
                school.magnet = True
                school.save()

    def handle(self, *args, **options):
        download = options['download']
        if download:
            os.mkdir(DUMP_DIR)
        self.load_school_points(download)
        self.load_districts(download)
        self.load_walkzones(download)
