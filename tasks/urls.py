from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page
from homesite import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),    
)