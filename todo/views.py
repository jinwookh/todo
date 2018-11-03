from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.utils.timezone import datetime


from .models import Todo, CompletedTodo
from .form import PostForm



def index(request):
#This function has to give todo objects in todo LIST to index.html
#shows todo LIST in order of priority
    todoList = Todo.objects.order_by('priority')

    expiredList = Todo.objects.filter(due_date__lte = datetime.today())
    context = {
        'todo_list':todoList,
        'expired_list': expiredList,
    }

    return render(request, 'todo/index.html', context)

def detail(request, todo_id):
#this function has to give id of todo object to detail.html
    try:
        todo =  Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        raise Http404("Chosen Todo does not exist")
    return render(request, 'todo/detail.html', {'todo':todo})

def checkComplete(request, todo_id):
    #at here, generates completedTodo object having same information with givin todo object,
    #deletes the given todo object, and redirect to todo:index
    todo = get_object_or_404(Todo, pk=todo_id)
    completed = CompletedTodo()
    completed.todo_title = todo.todo_title
    completed.text = todo.text
    completed.priority = todo.priority
    completed.due_date = todo.due_date
    completed.save()
    todo.delete()

    return redirect('todo:index')

def adjust(request, todo_id):
#at this method, when request is not post, it renders adjust.html
#if request is post, adjusts new information with corresponding todo object
#and then renders adjustment.html with error code
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = todo)
        #above code is 1st major difference between create function and adjust function
        if form.is_valid():
            todo = form.save()
            return render(request, 'todo/adjustment.html',{'error':0})
        else:
            return render(request, 'todo/adjustment.html', {'error':1})

    else:
        form = PostForm(instance = todo)
        #above code is 2nd major difference between create function and adjust function
        return render(request, 'todo/create.html', {'form': form})

def delete(request, todo_id):
    #delete the object corresponding to todo_id
    #and redirect todo:index
    todo = get_object_or_404(Todo,pk=todo_id)
    title = todo.todo_title
    todo.delete()
    return render(request, 'todo/deletion.html', {'title' : title})

def finishedList(request):
#this function shows list of completedTodo objects in order of due_date
    finishedList = CompletedTodo.objects.order_by('due_date')
    context = {
        'finished_list':finishedList
    }

    return render(request, 'todo/finishedList.html', context)

def create(request):
    #at this method, when request is not post, it renders creat.html
    #if request is post, generates form with information of request.POST,
    #with the form, generates object at DB,
    #and then renders creation.html with error code
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid() :
            todo = form.save(commit=False)
            todo.save()
            context = {
            'error_value' : 0
            }
            return render(request, 'todo/creation.html', context)

        else:
            context = {
            'error_value' : 1
            }
            return render(request, 'todo/creation.html', context)

    else:
        form = PostForm()
        return render(request, 'todo/create.html', {'form': form})
