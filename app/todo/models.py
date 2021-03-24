from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name