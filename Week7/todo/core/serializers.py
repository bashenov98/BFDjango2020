from rest_framework import serializers


from auth_.serializers import CustomUserSerializer
from core.models import ToDoList, ToDo, ToDoCategory


def name_validator(name):
    for n in name:
        if not (n.isalpha() or n == " "):
            raise ValueError(f'{n} character is not permitted in NAME field')

def status_validator(status):
    if status not in [0, 1, 2, 3]:
        raise ValueError(f'{status} is not exist')

def favorites_validator(favorite):
    if favorite != True or favorite != False:
        raise ValueError(f'{favorite} status is not correct')


class ToDoListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, validators=[name_validator])
    favorite = serializers.BooleanField(required=False, validators=[favorites_validator])
    owner = CustomUserSerializer(read_only=True)

    class Meta:
        model = ToDoList
        fields = ('id', 'name', 'owner', 'favorite' )


class ToDoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    name = serializers.CharField(required=True, validators=[name_validator])
    list = ToDoListSerializer(read_only=True)
    status = serializers.IntegerField(validators=[status_validator])

    class Meta:
        model = ToDo
        fields = ('id', 'name', 'created_at', 'due_on', 'is_done', 'list', 'notes', 'status')

class ToDoDetailedSerializer(serializers.ModelSerializer):
    todo_list_full = ToDoListSerializer(read_only=True)

    class Meta(ToDoSerializer.Meta):
        fields = ToDoSerializer.Meta.fields + ('todo_list_full',)

class WorkToDoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, validators=[name_validator])
    todo = serializers.IntegerField(read_only=True)

    class Meta:
        model = ToDoCategory
        field = ('id', 'name', 'todo')

class StudyToDoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, validators=[name_validator])
    todo = serializers.IntegerField(read_only=True)

    class Meta:
        model = ToDoCategory
        field = ('id', 'name', 'todo')

