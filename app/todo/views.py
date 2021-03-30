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

def updatetask(request,id):
    if request.method == 'POST':
        try:
            # id = request.POST["id"]
            name = request.POST["name"]
            todoid = request.POST["todo_id"]
            done = request.POST.get('done', False)

            task = Task.objects.get(id=id)
            print("TaSK :" + str(id))
            print("TaSK Name :" + name )
            print("TaSK Done :" +  str(done) )

        except Task.DoesNotExist:
            task = None
        
        form = TaskForm(instance=task, data=request.POST)
        print("TaSK 3 :" )
        if form.is_valid():
            print("TaSK 4 :" )
            form.save()
            print("TaSK 5 :" )
            return HttpResponseRedirect('/todo/'+str(todoid))
            # return HttpResponseRedirect('/todo/')

    else:
        form = TaskForm()

    context = {
        'form':form
    }
    print("TaSK 6 :" )
    return render(request, 'todo/task.html' , context)