from rest_framework import viewsets, permissions

from .models import TodoItem
from .serializers import TodoItemSerializer


class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodoItemSerializer