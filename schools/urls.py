from django.conf.urls import patterns, url

from schools.views import ActiveSchools, SchoolDetail


school_urls = patterns('',
    url(r'detail/(?P<pk>[0-9]+)/$', SchoolDetail.as_view(), name='school-detail'),
    url(r'$', ActiveSchools.as_view(), name='all-schools'),
)
