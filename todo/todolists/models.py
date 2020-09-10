from django.db import models


class TodoList(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TodoItem(models.Model):
    title = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    todoList = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.title