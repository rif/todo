from annoying.decorators import render_to, ajax_request
from annoying.functions import get_object_or_None
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import CreateView, UpdateView
from tasks.forms import TaskForm
from tasks.models import Task
from django.shortcuts import redirect

@render_to('tasks/index.html')
def index(request):
	return locals()

class TaskCreateView(CreateView):
	form_class = TaskForm	
	template_name = 'tasks/new.html'
	success_url = 'tasks:index'

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()

		return redirect('/')

class TaskUpdateView(UpdateView):
	form_class = TaskForm	
	template_name = 'tasks/new.html'
	success_url = 'tasks:index'
	

@ajax_request
def incr_priority(request, task_id):
	task = get_object_or_None(Task, id=task_id)
	if not task: return 0
	if request.user != task.user:
		raise PermissionDenied()
	task.priority += 1
	task.save()
	return {'p': task.priority}

@ajax_request
def decr_priority(request, task_id):
	task = get_object_or_None(Task, id=task_id)
	if not task: return 0
	if request.user != task.user:
		raise PermissionDenied()
	task.priority -= 1
	task.save()
	return {'p': task.priority}

@ajax_request
def delete(request, task_id):
	task = get_object_or_None(Task, id=task_id)
	if not task: return 0
	if request.user != task.user:
		raise PermissionDenied()
	task.delete()
	return {'r': "ok"}