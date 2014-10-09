from django.conf.urls import patterns, url

from schools.views import AssignedSchools, OptionSchools, AllSchools


school_urls = patterns('',
    url(r'assigned/$', AssignedSchools.as_view(), name='assigned-schools'),
    url(r'option/$', OptionSchools.as_view(), name='option-schools'),
    url(r'all', AllSchools.as_view(), name='all-schools')
)
