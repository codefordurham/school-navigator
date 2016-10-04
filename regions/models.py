from django.contrib.gis.db import models as gis
from django.db import models


class Region(gis.Model):
    """Geographical regions"""
    TYPE_CHIOCES = (
        ('country', 'Country'),
        ('state', 'State'),
        ('county', 'County'),
    )
    name = models.CharField(max_length=255)
    alternate_name = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=16, choices=TYPE_CHIOCES,
                            default='county')
    external_id = models.IntegerField("External ID")
    boundary = gis.MultiPolygonField()

    objects = gis.GeoManager()

    class Meta(object):
        unique_together = ('external_id', 'type')

    def __unicode__(self):
        return u"{} - {}".format(self.get_type_display(), self.name)
