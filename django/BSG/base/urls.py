from django.conf.urls import patterns, url, include
from base import views
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers, routers

router = routers.SimpleRouter()
router.register(r'', views.BusinessProjectSet)


urlpatterns = patterns('',
    url(r'^main', views.main, name='main'),
    url(r'^company', company.as_view()),
    url(r'^production', production.as_view()),
    url(r'^product', product.as_view()),
    url(r'^finance', finance.as_view()),
    url(r'^marketing', marketing.as_view()),
    url(r'^hr', hr.as_view()),
    url(r'^api', include(router.urls)),
)
