from rest_framework import serializers
from rest_framework_gis import serializers as geo_serializers

import schools.models as schools_models

class SchoolListSerializer(geo_serializers.GeoModelSerializer):
    eligibility = serializers.SerializerMethodField('get_eligibility')

    class Meta:
        model = schools_models.School
        fields = ('id', 'name', 'level', 'address', 'type', 'eligibility', 'location')

    def get_eligibility(self, obj):
        pt = self.context['point']
        if obj.district is not None and obj.district.contains(pt):
            return 'assigned'
        if obj.walk_zone is not None and obj.walk_zone.contains(pt):
            #TODO set highlight color
            return 'assigned'
        if obj.type == 'magnet':
            return 'option'
        if obj.type == 'charter':
            return 'option'
        return 'all'

class SchoolDetailSerializer(geo_serializers.GeoModelSerializer):
    class Meta:
        model = schools_models.School
