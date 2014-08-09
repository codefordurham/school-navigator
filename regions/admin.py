from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from . import models


class RegionAdmin(LeafletGeoAdmin):
    list_display = ['name', 'alternate_name', 'type']
    list_filter = ['type']
    ordering = ['type', 'name']
    search_fields = ['name', 'alternate_name', 'external_id']


admin.site.register(models.Region, RegionAdmin)
