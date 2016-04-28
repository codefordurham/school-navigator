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
    short_name = serializers.SerializerMethodField('get_short_name')
    level = serializers.SerializerMethodField('get_level')
    year_round = serializers.SerializerMethodField('get_level')
    grade_min = serializers.SerializerMethodField('get_grade_min')
    grade_max = serializers.SerializerMethodField('get_grade_max')
    website_url = serializers.SerializerMethodField('get_website_url')
    mission_statement = serializers.SerializerMethodField('get_mission_statement')
    preference_type = serializers.SerializerMethodField('get_preference_type')
    survey_hash = serializers.SerializerMethodField('get_survey_hash')

    class Meta:
        model = schools_models.School
        fields = ('id', 'name', 'level', 'address', 'type', 'location', 'short_name',
                  'year_round', 'grade_min', 'grade_max', 'website_url',
                  'active', 'mission_statement', 'preference_type',
                  'survey_hash')

    def get_level(self, obj):
        school_profile = obj.profile()
        return school_profile.level if school_profile else ''

    def get_grade_min(self, obj):
        school_profile = obj.profile()
        return school_profile.grade_min if school_profile else ''

    def get_year_round(self, obj):
        school_profile = obj.profile()
        return school_profile.year_round if school_profile else ''

    def get_grade_max(self, obj):
        school_profile = obj.profile()
        return school_profile.grade_max if school_profile else ''

    def get_website_url(self, obj):
        school_profile = obj.profile()
        return school_profile.website_url if school_profile else ''

    def get_mission_statement(self, obj):
        school_profile = obj.profile()
        return school_profile.mission_statement if school_profile else ''

    def get_survey_hash(self, obj):
        survey = obj.schoolprofile_set.order_by('submitted_at').last()
        if survey:
            return survey.url()
        else:
            return ''

    def get_short_name(self, obj):
        if obj.short_name:
            return obj.short_name
        words = [word.upper() for index, word in enumerate(obj.name.split(' ')) if index <= 1]
        if len(words) == 1:
            name = words[0]
            return "".join([name[0], name[1]])
        return "".join(map(lambda word: word[0], words))

    def get_preference_type(self, obj):
        """Returns the type of preference you have ito be admitted in school"""
        if obj.walk_zone:
            return u'walk zone'
        elif obj.choice_zone:
            return u'choice zone'
        elif obj.priority_zone:
            return u'priority zone'
        elif obj.year_round_zone:
            return u'year round option'
        elif obj.district:
            return u'neighborhood'
        return ''

class LocalSchoolListSerializer(SchoolListSerializer):
    """
    A school with additionial information relative to the query point
    """

    distance = serializers.SerializerMethodField('get_distance')
    eligibility = serializers.SerializerMethodField('get_eligibility')
    preference = serializers.SerializerMethodField('get_preference')

    class Meta:
        model = schools_models.School
        fields = ('id', 'name', 'level', 'address', 'type', 'eligibility',
                  'location', 'preference', 'short_name', 'distance',
                  'year_round', 'grade_min', 'grade_max', 'website_url',
                  'active', 'mission_statement', 'preference_type',
                  'survey_hash')


    def get_distance(self, obj):
        return obj.distance.mi

    def get_eligibility(self, obj):
        pt = self.context['point']
        if obj.district is not None and obj.district.contains(pt):
            return 'assigned'
        if obj.walk_zone is not None and obj.walk_zone.contains(pt):
            return 'assigned'
        if obj.choice_zone is not None and obj.choice_zone.contains(pt):
            return 'assigned'
        if obj.year_round_zone is not None and obj.year_round_zone.contains(pt):
            return 'option'
        if obj.traditional_option_zone is not None and obj.traditional_option_zone.contains(pt):
            return 'assigned'
        if obj.type in ('magnet', 'charter', 'speciality'):
            return 'option'
        raise Exception

    def get_preference(self, obj):
        pt = self.context['point']
        # return auto-assigned (walk/choice) before other zones
        # see https://github.com/codefordurham/school-navigator/pull/217
        if obj.district is not None and obj.district.contains(pt):
            return 'neighborhood'
        if obj.walk_zone is not None and obj.walk_zone.contains(pt):
            return 'walk zone'
        if obj.choice_zone is not None and obj.choice_zone.contains(pt):
            return 'choice'
        if obj.priority_zone is not None and obj.priority_zone.contains(pt):
            return 'priority'
        if obj.year_round_zone is not None and obj.year_round_zone.contains(pt):
            return 'year round option'
        if obj.traditional_option_zone is not None and obj.traditional_option_zone.contains(pt):
            return 'traditional calendar option'


class SchoolProfileSerilaizer(serializers.ModelSerializer):
    lunch_served_display = serializers.CharField(source='get_lunch_served_display')
    transportation_display = serializers.CharField(source='get_transportation_display')
    breakfast_served_display = serializers.CharField(source='get_breakfast_served_display')
    get_lottery_priority_1_display = serializers.CharField(source='get_lottery_priority_1_display')
    get_lottery_priority_2_display = serializers.CharField(source='get_lottery_priority_2_display')
    get_lottery_priority_3_display = serializers.CharField(source='get_lottery_priority_3_display')
    get_lottery_priority_4_display = serializers.CharField(source='get_lottery_priority_4_display')
    get_lottery_priority_5_display = serializers.CharField(source='get_lottery_priority_5_display')

    class Meta:
        model = schools_models.SchoolProfile



class SchoolDetailSerializer(geo_serializers.GeoModelSerializer):
    color = serializers.SerializerMethodField('get_color')
    survey_hash = serializers.SerializerMethodField('get_survey_hash')
    grades = serializers.SerializerMethodField('get_grades')
    school_type = serializers.CharField(source='get_type_display')
    profile = SchoolProfileSerilaizer()

    class Meta:
        model = schools_models.School

    def get_color(self, obj):
        return COLOR_MAP.get(obj.profile().level, 'purple')

    def get_survey_hash(self, obj):
        survey = obj.schoolprofile_set.order_by('submitted_at').last()
        if survey:
            return survey.url()
        else:
            return ''

    def get_grades(self, obj):
        return "{0} - {1}".format(obj.profile().get_grade_min_display(), obj.profile().get_grade_max_display())
