from django.contrib import admin
from .models import Todo, CompletedTodo
# Register your models here.
admin.site.register(Todo)
admin.site.register(CompletedTodo)
