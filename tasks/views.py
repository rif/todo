from annoying.decorators import render_to

@render_to('tasks/index.html')
def index(request):
	return locals()