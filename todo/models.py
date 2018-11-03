from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Todo(models.Model):
    todo_title = models.CharField(max_length = 50)
    due_date = models.DateTimeField(blank=True, null=True, default = 0)

    priority = models.IntegerField(validators=[MinValueValidator(0),], default = 5)
    text = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.todo_title

class CompletedTodo(models.Model):
    todo_title = models.CharField(max_length = 50)
    due_date = models.DateTimeField(blank=True, null=True, default = 0)

    priority = models.IntegerField(validators=[MinValueValidator(0),], default = 5)
    text = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.todo_title
