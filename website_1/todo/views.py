from django.http import HttpResponse
from django.template import Context, loader

from .models import Todo


def index(request):
    todos = Todo.objects.all()
    t = loader.get_template('todo/base.html')
    c = Context({'todos': todos})
    return HttpResponse(t.render(c))
