from django.shortcuts import render
from .models import Todo

def index(request):
#This function has to give todo objects in todo LIST to index.html
    todoList = Todo.objects.all.order_by('-priority')
    context = {
        'todo_list':todoList
    }

    return render(request, 'todo/index.html', context)

def detail(request, todo_id):

    return render(request, 'todo/detail.html')

def checkComplete(request, todo_id):


    return HttpResponseRedirect('todo:index')

def adjust(request, todo_id):


    return render(request, 'todo/adjust.html')

def delete(request, todo_id):

    return render(request, 'todo/delete.html')

def finishedList(request):

    return render(request, 'todo/finishedList.html')

def create(request):

    return render(request, 'todo/create.html')

def creation(request):

    return render(request, 'todo/creation.html')

def adjustment(request):

    return render(request, 'todo/adjustment.html')
