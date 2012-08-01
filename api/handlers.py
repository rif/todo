import re

from piston.handler import BaseHandler
from piston.utils import rc, throttle

from tasks.models import Task

class TaskHandler(BaseHandler):
    "handles operations for specific tasks (view/edit/delete)"
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    fields = ('title', 'creation_date', 'priority')
    exclude = ('id', re.compile(r'^private_'))
    model = Task

    @classmethod
    def content_size(self, task):
        return len(task.title)

    def read(self, request, task_id):
        if task_id:
            result = Task.objects.get(pk=task_id)
        else:
            result = Task.objects.filter(user=request.user)        
        return result

    def create(self, request, task_id):
        if 'title' not in request.POST:
            return rc.BAD_REQUEST
        task = Task()
        task.title = request.POST.get('title')
        task.priority =  int(request.POST.get('priority')) if request.POST.get('priority') else 0
        task.user = request.user
        task.save()

        return rc.CREATED

    @throttle(5, 10*60) # allow 5 times in 10 minutes
    def update(self, request, task_id):        
        task = Task.objects.get(pk= task_id)

        if not request.user ==  task.user:
            return rc.FORBIDDEN # returns HTTP 401
            
        task.title = request.PUT.get('title') or  task.title
        task.priority = int(request.PUT.get('priority')) if request.PUT.get('priority') else task.priority
        task.save()

        return task

    def delete(self, request, task_id):
        task = Task.objects.get(pk= task_id)

        if not request.user ==  task.user:
            return rc.FORBIDDEN # returns HTTP 401

        task.delete()

        return rc.DELETED # returns HTTP 204
