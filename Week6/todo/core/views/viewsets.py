from core.models import ToDo, ToDoList
from core.serializers import ToDoSerializer,ToDoListSerializer

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action


class ToDoListViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer

    @action(methods=['GET'], detail=False)
    def favorites(self):
        chosen = ToDoList.objects.filter(favorite=True)
        serializer = ToDoListSerializer(chosen)
        return Response(serializer.data)

    @action(methods=['PUT'], detail=True)
    def set_star(self, request, pk):
        chosen_todolist = get_object_or_404(ToDoList, id=pk)
        chosen_todolist.self.favorite = True
        serializer = ToDoListSerializer(chosen_todolist)
        return Response(serializer.data)
