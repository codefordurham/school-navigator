from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from .models import School

class SchoolAdmin(LeafletGeoAdmin):
    list_display = ('name', 'level', 'type', 'year_round')
    ordering = ('name',)
    list_filter = ('year_round', 'level', 'type')

admin.site.register(School, SchoolAdmin)
