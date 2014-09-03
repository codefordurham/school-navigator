from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from schools.urls import school_urls

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^api/schools/', include(school_urls)),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
