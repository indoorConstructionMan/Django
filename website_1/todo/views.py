from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.views import generic
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from .models import Todo

def index(request):
    todos = Todo.objects.all()
    return render_to_response('todo/index.html', {'todos': todos}, context_instance=RequestContext(request))

def create(request):
    todos = Todo.objects.all()
    t = loader.get_template('todo/create.html')
    c = Context({'todos': todos})
    c.update(csrf(request))
    return HttpResponse(t.render(c))
