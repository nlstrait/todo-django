from rest_framework import serializers
from .models import TodoList, TodoItem


# Todo Item Serializer
class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['id', 'title', 'done', 'created']

# Todo List Serializer
class TodoListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 100)
    created = serializers.DateTimeField()
    todoitem_set = TodoItemSerializer(many=True)
