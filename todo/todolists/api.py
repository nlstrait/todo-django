from rest_framework import viewsets, permissions

from .models import TodoList
from .serializers import TodoListSerializer


# TodoList ViewSet
class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodoListSerializer