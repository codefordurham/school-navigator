from django.contrib.gis.db import models

ELEM = 1
MID = 2
SEC = 3
HIGH = 4
SCHOOL_LEVELS = (
    (ELEM, 'Elementary'),
    (MID, 'Middle'),
    (SEC, 'Secondary'),
    (HIGH, 'High')
)


class School(models.Model):
    name = models.CharField(max_length=100, unique=True)
    level = models.IntegerField(choices=SCHOOL_LEVELS, default=4)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=5)
    magnet = models.BooleanField(default=False)
    #Type = Neighborhood, Magnet, Charter
    year_round = models.BooleanField(default=False)
    location = models.PointField()
    district = models.PolygonField(null=True)

    # Zones per http://dpsncapplication.com/site327.php
    walk_zone = models.PolygonField(null=True)
    choice_zone =  models.PolygonField(null=True)
    priority_zone = models.PolygonField(null=True)

    # Override default manager for gis
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name
