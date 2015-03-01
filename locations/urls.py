from django.conf.urls import patterns, url

from locations import views

urlpatterns = patterns('',
  url(r'^$', views.locations, name='locations'),
)
