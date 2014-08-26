from django.contrib import admin
from school_inspector.schools.models import School 

class SchoolAdmin(admin.ModelAdmin):
        pass

admin.site.register(School, SchoolAdmin)
