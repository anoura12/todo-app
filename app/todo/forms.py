from django.forms import ModelForm
from django import forms
from .models import Todo,Task

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name','done']
