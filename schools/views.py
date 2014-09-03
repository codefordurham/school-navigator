from django.shortcuts import render
from django.contrib.gis.geos import Point

from rest_framework import generics

from schools.serializers import SchoolSerializer
from schools import models as schools_models

class LocationEligibleSchools(generics.ListAPIView):
    model = schools_models.School
    serializer_class = SchoolSerializer

    def get_queryset(self):
        queryset = super(LocationEligibleSchools, self).get_queryset()
        lat, lon = self.request.GET['location'].split(',')
        pt = Point(float(lat), float(lon))
        return queryset.filter(district__contains=pt)
