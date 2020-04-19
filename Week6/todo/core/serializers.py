from rest_framework import serializers

from rest_framework import serializers

from auth_.serializers import CustomUserSerializer
from core.models import ToDoList, ToDo


class ToDoListSerializer(serializers.ModelSerializer):

    owner = CustomUserSerializer(read_only=True)

    class Meta:
        model = ToDoList
        fields = ('id', 'name', 'owner', )


class ToDoSerializer(serializers.ModelSerializer):

    list = ToDoListSerializer(read_only=True)

    class Meta:
        model = ToDo
        fields = ('id', 'name', 'created_at', 'due_on', 'is_done', 'list', 'notes')
