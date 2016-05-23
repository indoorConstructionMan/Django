from django.db import models

class Todo(models.Model):
    todo_description = models.TextField()
    todo_completed = models.BooleanField()

    def __str__(self):
        return self.todo_description
