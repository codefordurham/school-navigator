from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from .models import School


class SchoolAdmin(LeafletGeoAdmin):
    list_display = ('name', 'photo', 'type')
    ordering = ('name',)
    list_filter = ('type', )

admin.site.register(School, SchoolAdmin)
