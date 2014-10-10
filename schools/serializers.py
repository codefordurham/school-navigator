from rest_framework import serializers
from rest_framework_gis import serializers as geo_serializers

import schools.models as schools_models

class SchoolSerializer(geo_serializers.GeoModelSerializer):
    type = serializers.SerializerMethodField('get_type')

    class Meta:
        model = schools_models.School
        #TODO Add back district?
        fields = ('id', 'name', 'level', 'address', 'magnet', 'type')

    def get_type(self, obj):
       import random
       return random.choice(('assigned', 'option', 'all'))
