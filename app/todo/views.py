from django.shortcuts import get_object_or_404,render
from .forms import TodoForm,TaskForm
from django.http import HttpResponseRedirect
from .models import Todo,Task
# Create your views here.
def todo(request):
    todolist = Todo.objects.all()
    todoform = TodoForm()

    context = {
        'todolist':todolist,
        'form':todoform
    }
    return render(request, 'todo/todo.html', context)

def task(request,todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todotasks = Task.objects.filter(todo=todo_id)
    taskform = TaskForm()

    context = {
        'todotasks': todotasks,
        'todo': todo,
        'form': taskform
    }
    return render(request, 'todo/task.html', context)

def addtodo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)   
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/todo/')
    else:
        form = TodoForm()
   
    context = {
    'form': form
  }

    return render(request, 'todo/todo.html', context)

def addtask(request,id):
    if request.method == 'POST':
        task = Task(todo_id=id)
        form = TaskForm(instance=task, data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/todo/'+str(id))

    else:
        form = TaskForm()

    context = {
        'form':form
    }

    return render(request, 'todo/task.html' , context)

def taskdone(request,id):
    print("hello")
    if request.method == 'POST':
        task = Task.objects.get(pk=id)
        form = TaskForm(instance=task, data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/todo/'+str(id))

    else:
        form = TaskForm()

    context = {
        'form':form
    }

    return render(request, 'todo/task.html' , context)