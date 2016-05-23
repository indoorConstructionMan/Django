from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('todo_description', 'todo_completed')

admin.site.register(Todo, TodoAdmin)
