from rest_framework import serializers
from rest_framework_gis import serializers as geo_serializers

import schools.models as schools_models

COLOR_MAP = {
    'elementary': '#48BC6B',
    'middle': '#3F899E',
    'secondary': '#3F899E',
    'high': '#4F61AD'
}


class SchoolListSerializer(geo_serializers.GeoModelSerializer):
    eligibility = serializers.SerializerMethodField('get_eligibility')
    preference = serializers.SerializerMethodField('get_preference')
    short_name = serializers.SerializerMethodField('get_short_name')
    distance = serializers.SerializerMethodField('get_distance')

    class Meta:
        model = schools_models.School
        fields = ('id', 'name', 'level', 'address', 'type', 'eligibility',
                  'location', 'preference', 'short_name', 'distance',
                  'year_round', 'grade_min', 'grade_max', 'website_url',
                  'active', 'mission_statement')

    def get_eligibility(self, obj):
        pt = self.context['point']
        if obj.district is not None and obj.district.contains(pt):
            return 'assigned'
        if obj.walk_zone is not None and obj.walk_zone.contains(pt):
            return 'assigned'
        if obj.type in ('magnet', 'charter', 'speciality'):
            return 'option'
        raise Exception

    def get_preference(self, obj):
        pt = self.context['point']
        if obj.priority_zone is not None and obj.priority_zone.contains(pt):
            return 'priority'
        if obj.choice_zone is not None and obj.choice_zone.contains(pt):
            return 'choice'

    def get_short_name(self, obj):
        if obj.short_name:
            return obj.short_name
        words = [word.upper() for index, word in enumerate(obj.name.split(' ')) if index <= 1]
        if len(words) == 1:
            name = words[0]
            return "".join([name[0], name[1]])
        return "".join(map(lambda word: word[0], words))

    def get_distance(self, obj):
        return obj.distance.mi


class SchoolDetailSerializer(geo_serializers.GeoModelSerializer):
    color = serializers.SerializerMethodField('get_color')

    class Meta:
        model = schools_models.School

    def get_color(self, obj):
        return COLOR_MAP.get(obj.level, 'purple')
