from django.conf.urls import patterns, url, include

from schools.views import LocationEligibleSchools


school_urls = patterns('',
    url(r'eligibleschools$', LocationEligibleSchools.as_view(), name='eligible-schools')
)
