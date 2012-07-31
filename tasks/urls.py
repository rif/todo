from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView
from tasks import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),                
    url(r'^new/$', views.task_edit, name='new'),
    url(r'^edit/(?P<task_id>\d+)/$', views.task_edit, name='edit'),
    url(r'^about/$', TemplateView.as_view(template_name='tasks/about.html'), name='about'),
	url(r'^incr/(?P<task_id>\d+)/$', views.incr_priority, name='incr'),
	url(r'^decr/(?P<task_id>\d+)/$', views.decr_priority, name='decr'),
	url(r'^delete/(?P<task_id>\d+)/$', views.delete, name='delete'),
)