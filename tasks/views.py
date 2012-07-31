# Create your views here.

@render_to('tasks/index.html')
def index(request):
	return locals()