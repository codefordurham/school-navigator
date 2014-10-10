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

class AssignedSchools(SchoolAPIView):
    """
    pt is in school districts or walkzones
    """

    def get_queryset(self):
        queryset = super(AssignedSchools, self).get_queryset()
        return queryset.filter(Q(district__contains=self.pt) | Q(walk_zone__contains=self.pt))

class OptionSchools(SchoolAPIView):
    """
    Magnets (except where pt is in Walkzone), Charters
    """

    def get_queryset(self):
        queryset = super(OptionSchools, self).get_queryset()
        #TODO highlight Schools where pt in priority_zone or choice_zone
        # (Type == Magnet && walk_zone != contain pt) || Type = Charter
        return queryset.filter(district=None).exclude(walk_zone__contains=self.pt)

class AllSchools(SchoolAPIView):
    """
    Both Assigned And Option Schools
    """

    def get_queryset(self):
        queryset = super(AllSchools, self).get_queryset()
        #TODO
        #Assigned schools are blue
        #Option schools are orange
        #Others are gray
        return queryset
