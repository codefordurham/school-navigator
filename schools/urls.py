from django.conf.urls import patterns, url

from schools.api import ActiveSchools, SchoolDetail, SchoolProfileDetail

school_urls = patterns('',
    url(r'detail/(?P<pk>[0-9]+)/$', SchoolDetail.as_view(), name='school-detail'),
    url(r'survey/(?P<pk>\w+)/$', SchoolProfileDetail.as_view(), name='school-survey'),
    url(r'$', ActiveSchools.as_view(), name='all-schools'),
)
