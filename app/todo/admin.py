from django.contrib import admin
from .models import Todo,Task

class TodoAdmin(admin.ModelAdmin):
    fields = ['name']


admin.site.register(Todo,TodoAdmin)
admin.site.register(Task)

