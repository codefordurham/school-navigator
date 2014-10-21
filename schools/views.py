from django.contrib.gis.geos import Point
from django.db.models import Q

from rest_framework import generics
from rest_framework.exceptions import ParseError

from schools.serializers import SchoolSerializer
from schools import models as schools_models

class SchoolAPIView(generics.ListAPIView):
    model = schools_models.School
    serializer_class = SchoolSerializer

    def get_queryset(self):
        queryset = super(SchoolAPIView, self).get_queryset()
        try:
            lat = self.request.GET['latitude']
            lon = self.request.GET['longitude']
            pt = Point(float(lon), float(lat))
        except ValueError:
            raise ParseError("Bad location")
        except KeyError:
            raise ParseError("No location provided")
        self.pt = pt
        return queryset

    def get_serializer_context(self):
        context = super(SchoolAPIView, self).get_serializer_context()
        context['point'] = self.pt
        return context

class AllSchools(SchoolAPIView):
    """
    Both Assigned And Option Schools
    """

    def get_queryset(self):
        queryset = super(AllSchools, self).get_queryset()
        queryset.filter(
                Q(district__contains=self.pt) |
                Q(type='magnet') |
                Q(type='specialty') |
                Q(type='charter')
        )
        return queryset
