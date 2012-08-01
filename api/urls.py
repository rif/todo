from django.conf.urls import patterns, include, url
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication

from api.handlers import TaskHandler

auth = HttpBasicAuthentication(realm="Todo Realm")
ad = { 'authentication': auth }

task_resource = Resource(handler=TaskHandler, **ad)

urlpatterns = patterns('',
    url(r'^tasks/(?P<task_id>\d+)/$', task_resource), 
    )
