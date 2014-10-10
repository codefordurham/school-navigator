from django.conf.urls import patterns, url

from schools.views import AllSchools


school_urls = patterns('',
    url(r'$', AllSchools.as_view(), name='all-schools')
)
