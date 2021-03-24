from django.urls import path
from . import views

app_name = 'todo'
urlpatterns =[
    path('', views.todo, name='todo'),
    path('<int:todo_id>/', views.task,name ='task'),
    path('addtodo/', views.addtodo, name='addtodo'),
    path('addtask/<int:id>/', views.addtask, name='addtask'),
    path('taskdone/<int:id>/', views.taskdone, name='taskdone'),

]