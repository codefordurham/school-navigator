from django.contrib.gis.geos import Point
from django.db.models import Q

from rest_framework import generics
from rest_framework.exceptions import ParseError

from schools.serializers import SchoolSerializer
from schools import models as schools_models

def parse_latlon(request):
    try:
        lat = request.GET['latitude']
        lon = request.GET['longitude']
        pt = Point(float(lon), float(lat))
    except ValueError:
        raise ParseError("Bad location")
    except KeyError:
        raise ParseError("No location provided")
    return pt

class AssignedSchools(generics.ListAPIView):
    """
    pt is in school districts or walkzones
    """
    model = schools_models.School
    serializer_class = SchoolSerializer

    def get_queryset(self):
        queryset = super(AssignedSchools, self).get_queryset()
        pt = parse_latlon(self.request)
        return queryset.filter(Q(district__contains=pt) | Q(walk_zone__contains=pt))

class OptionSchools(generics.ListAPIView):
    """
    Magnets (except where pt is in Walkzone), Charters
    """
    model = schools_models.School
    serializer_class = SchoolSerializer

    def get_queryset(self):
        queryset = super(OptionSchools, self).get_queryset()
        pt = parse_latlon(self.request)
        return queryset.filter(district=None).exclude(walk_zone__contains=pt)

class AllSchools(generics.ListAPIView):
    """
    Both Assigned And Option Schools
    """
    model = schools_models.School
    serializer_class = SchoolSerializer

    def get_queryset(self):
        queryset = super(AllSchools, self).get_queryset()
        pt = parse_latlon(self.request)
        return queryset.filter(district=None).exclude(walk_zone__contains=pt)
