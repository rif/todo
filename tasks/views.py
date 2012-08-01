from annoying.decorators import render_to, ajax_request
from annoying.functions import get_object_or_None
from django.core.exceptions import PermissionDenied
from tasks.forms import TaskForm
from tasks.models import Task
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@render_to('tasks/index.html')
def index(request):
    "listst the tasks with pagination"
    tasks = []
    if request.user.is_authenticated():
        tasks = Task.objects.filter(user=request.user)
    paginator = Paginator(tasks, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tasks = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        tasks = paginator.page(paginator.num_pages)    
    return locals()

@render_to('tasks/new.html')
@login_required
def task_edit(request, task_id=None):
    "used for both creation and editing of a task"
    task = None
    if task_id:
        task = get_object_or_None(Task, pk=task_id)
    if task and task.user != request.user:
        raise PermissionDenied()
    if request.method == 'POST': 
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks:index')
    else:
        form = TaskForm(instance=task) 

    return locals()

@ajax_request
@login_required
def incr_priority(request, task_id):
    "ajax view for incremeneting the priority for a task"
    task = get_object_or_None(Task, id=task_id)
    if not task: return 0
    if request.user != task.user: raise PermissionDenied()
    task.priority += 1
    task.save()
    return {'p': task.priority}

@ajax_request
@login_required
def decr_priority(request, task_id):
    "ajax view for decrementing the priority for a task"
    task = get_object_or_None(Task, id=task_id)
    if not task: return 0
    if request.user != task.user: raise PermissionDenied()
    task.priority -= 1
    task.save()
    return {'p': task.priority}

@ajax_request
@login_required
def delete(request, task_id):
    "deletes the task"
    task = get_object_or_None(Task, id=task_id)
    if not task: return 0
    if request.user != task.user: raise PermissionDenied()
    task.delete()
    return {'r': "ok"}
