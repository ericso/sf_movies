from django.conf.urls import patterns, url

from locations import views

urlpatterns = patterns('',
  url(r'^$', 'locations.views.locations', name='locations'),
  # url(r'^$', views.locations, name='locations'),
)
