from django.db import models


class TodoItem(models.Model):
    title = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title