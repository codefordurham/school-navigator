from django.contrib.gis.geos import Point
from django.db.models import Q

from rest_framework import generics
from rest_framework.exceptions import ParseError

from schools.serializers import SchoolDetailSerializer, SchoolListSerializer
from schools import models as schools_models

class SchoolDetail(generics.RetrieveAPIView):
    model = schools_models.School
    serializer_class = SchoolDetailSerializer

class SchoolAPIView(generics.ListAPIView):
    model = schools_models.School
    serializer_class = SchoolListSerializer

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

class ActiveSchools(SchoolAPIView):
    """
    Both Assigned And Option Schools
    """

    def get_queryset(self):
        qs = super(ActiveSchools, self).get_queryset()
        qs = qs.filter(
                (~Q(district=None) & Q(district__contains=self.pt)) |
                Q(type__in=('magnet', 'speciality', 'charter'))
        )
        return qs.distance(self.pt)
