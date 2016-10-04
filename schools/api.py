from django.contrib.gis.geos import Point
from django.db.models import Q

from rest_framework import generics, serializers
from rest_framework.exceptions import ParseError

from schools.serializers import SchoolDetailSerializer, LocalSchoolListSerializer, SchoolListSerializer
from schools import models as schools_models

class SchoolProfileDetail(generics.RetrieveAPIView):
    model = schools_models.SchoolProfile

    def get_object(self):
        try:
            hashid = self.kwargs['pk']
            pk = schools_models.SchoolProfile.decode_url(hashid)
        except:
            raise ParseError("Bad survey reference")
        try:
            queryset = schools_models.SchoolProfile.objects.get(pk=pk)
        except:
            raise ParseError("Could not find survey")
        return queryset


class SchoolDetail(generics.RetrieveAPIView):
    model = schools_models.School
    serializer_class = SchoolDetailSerializer

class SchoolList(generics.ListAPIView):
    model = schools_models.School
    serializer_class = SchoolListSerializer

class LocalSchoolAPIView(generics.ListAPIView):
    model = schools_models.School
    serializer_class = LocalSchoolListSerializer

    def get_queryset(self):
        queryset = super(LocalSchoolAPIView, self).get_queryset()
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
        context = super(LocalSchoolAPIView, self).get_serializer_context()
        context['point'] = self.pt
        return context

class AllSchools(SchoolList):
    """
    List all active schools.
    """

    def get_queryset(self):
        qs = super(AllSchools, self).get_queryset()
        qs = qs.filter(active=True)
        qs = qs.order_by('name')
        return qs

class LocalSchools(LocalSchoolAPIView):
    """
    Both Assigned And Option Schools
    """

    def get_queryset(self):
        qs = super(LocalSchools, self).get_queryset()
        point_in_district = ~Q(district=None) & Q(district__contains=self.pt)
        option_schools = Q(type__in=('specialty', 'charter')) | (Q(type='magnet') & Q(year_round=False))
        # see https://github.com/codefordurham/school-navigator/issues/186
        option_magnet_year_round = Q(type='magnet') & Q(year_round_zone__contains=self.pt) & Q(year_round=True)
        # see https://github.com/codefordurham/school-navigator/issues/147
        traditional_options = Q(type="neighborhood") & Q(traditional_option_zone__contains=self.pt)
        q = point_in_district | option_schools | traditional_options | option_magnet_year_round
        qs = qs.filter(q)
        qs = qs.filter(active=True)
        return qs.distance(self.pt)
