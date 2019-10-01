from django.conf.urls import url

from schools.api import AllSchools, LocalSchools, SchoolDetail, SchoolProfileDetail

school_urls = [
    url(r'detail/(?P<pk>[0-9]+)/$', SchoolDetail.as_view(), name='school-detail'),
    url(r'survey/(?P<pk>\w+)/$', SchoolProfileDetail.as_view(), name='school-survey'),
    url(r'local/$', LocalSchools.as_view(), name='local-schools'),
    url(r'$', AllSchools.as_view(), name='all-schools'),
]
