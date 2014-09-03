from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from .models import School

class SchoolAdmin(LeafletGeoAdmin):
    list_display = ('name', 'level', 'magnet', 'year_round')
    ordering = ('name',)
    list_filter = ('level', 'magnet', 'year_round', 'zip_code')

admin.site.register(School, SchoolAdmin)
