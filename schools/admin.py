from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from .models import School

admin.site.register(School, LeafletGeoAdmin)
