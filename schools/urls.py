from django.conf.urls import patterns, url

from schools.views import AllSchools, SchoolDetail


school_urls = patterns('',
    url(r'detail/(?P<pk>[0-9]+)/$', SchoolDetail.as_view(), name='school-detail'),
    url(r'$', AllSchools.as_view(), name='all-schools'),
)
