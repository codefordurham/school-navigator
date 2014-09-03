from rest_framework import serializers

import schools.models as schools_models

class SchoolSerializer(serializers.ModelSerializer):
    """
    Serializing all the Books
    """
    class Meta:
        model = schools_models.School
        fields = ('id', 'name', 'level', 'address', 'magnet', 'district', 'location')
