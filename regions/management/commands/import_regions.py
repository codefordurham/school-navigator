import os
import io
import logging
import requests
import zipfile
import tempfile

from django.core.management.base import BaseCommand
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import MultiPolygon

from regions.models import Region


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """Download and import US Administrative Areas"""
    url = "http://biogeo.ucdavis.edu/data/gadm2/shp/USA_adm.zip"

    def download_and_unzip_data(self, destination):
        """Download zipped shapfiles"""
        logger.debug("Requesting {}".format(self.url))
        response = requests.get(self.url)
        archive = zipfile.ZipFile(io.BytesIO(response.content))
        logger.debug("Extracting archive into {}".format(str(destination)))
        archive.extractall(path=destination)

    def import_shapefile(self, shapefile, schema):
        """Load shapefile and import each feature"""
        logger.debug("Importing shapefile {}".format(shapefile))
        layer = DataSource(shapefile)[0]
        for feature in layer:
            fields = schema.from_feature(feature)
            Region.objects.create(**fields)

    def handle(self, *args, **options):
        Region.objects.all().delete()
        destination = tempfile.mkdtemp(prefix='regions')
        logger.debug("Created temp directory {}".format(destination))
        self.download_and_unzip_data(destination)
        for schema in (Country(), State(), County()):
            shapefile = os.path.join(destination, schema.filename)
            self.import_shapefile(shapefile, schema)


# Shapefile to Region mappings #

class Schema(object):
    """Basic class to convert shapefile features into Region models"""
    def from_feature(self, feature):
        fields = {
            'name': str(feature[getattr(self, 'name')]),
            'type': self.type,
            'external_id': str(feature[getattr(self, 'external_id')]),
            'boundary': feature.geom.geos,
        }
        if feature.geom.geom_type == 'Polygon':
            fields['boundary'] = MultiPolygon(feature.geom.geos)
        else:
            fields['boundary'] = feature.geom.geos
        if hasattr(self, 'alternate_name'):
            fields['alternate_name'] = str(feature[self.alternate_name])
        return fields


class Country(Schema):
    """Map country shapefile to Region model"""
    type = 'country'
    filename = 'USA_adm0.shp'
    # field name map:
    name = 'NAME_ENGLI'
    external_id = 'ID_0'


class State(Schema):
    """Map state shapefile to Region model"""
    type = 'state'
    filename = 'USA_adm1.shp'
    # field name map:
    name = 'NAME_1'
    external_id = 'ID_1'


class County(Schema):
    """Map County shapefile to Region model"""
    type = 'county'
    filename = 'USA_adm2.shp'
    # field name map:
    name = 'NAME_2'
    alternate_name = 'VARNAME_2'
    external_id = 'ID_2'
