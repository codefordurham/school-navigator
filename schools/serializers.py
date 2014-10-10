from rest_framework import serializers
from rest_framework_gis import serializers as geo_serializers

import schools.models as schools_models

class SchoolSerializer(geo_serializers.GeoModelSerializer):
    option = serializers.BooleanField(source='option')
    assigned = serializers.BooleanField(source='assigned')

    class Meta:
        model = schools_models.School
        fields = ('id', 'name', 'level', 'address', 'magnet', 'district',
                    'option', 'assigned')
