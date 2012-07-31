from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.decorators.cache import cache_page
from tasks import views
from tasks.models import Task

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
                    model=Task, 
                    paginate_by='5',
                    queryset=Task.objects.all(),
                    context_object_name="tasks",
                    template_name='tasks/index.html')),        
    url(r'^new/$', views.TaskCreateView.as_view(), name='new'),
    url(r'^edit/(?P<pk>\d+)/$', views.TaskUpdateView.as_view(), name='edit'),
	url(r'^incr/(?P<task_id>\d+)/$', views.incr_priority, name='incr'),
	url(r'^decr/(?P<task_id>\d+)/$', views.decr_priority, name='decr'),
	url(r'^delete/(?P<task_id>\d+)/$', views.delete, name='delete'),
)