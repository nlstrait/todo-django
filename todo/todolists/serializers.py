from rest_framework import serializers
from .models import TodoItem


# Todo Item Serializer
class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['id', 'title', 'completed', 'created']
