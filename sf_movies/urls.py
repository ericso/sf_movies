from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns('',

    url(r'^$', 'app.views.home', name='home'),
    url(r'^locations/', include('locations.urls')),

    # url(r'^admin/', include(admin.site.urls)),

    # hack for static files
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
