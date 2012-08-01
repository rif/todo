from django.conf.urls import patterns, include, url
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication

from api.handlers import TaskHandler, TaskListHandler

auth = HttpBasicAuthentication(realm="Todo Realm")
ad = { 'authentication': auth }

tasklist_resource = Resource(handler=TaskListHandler, **ad)
task_resource = Resource(handler=TaskHandler, **ad)

urlpatterns = patterns('',
    url(r'^tasks/$', tasklist_resource), 
    url(r'^task/(?P<task_id>\d+)/$', task_resource), 
    )
