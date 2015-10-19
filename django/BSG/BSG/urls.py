from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    #url(r'^$', 'BSG.views.index', name='index'),
    url(r'^$', include('landing.urls', namespace='landing')),
    url(r'^auth/', include('logsys.urls', namespace='rest_framework')),
    url(r'^base/', include('base.urls', namespace="base")),
    url(r'^admin/', include(admin.site.urls)),
]
