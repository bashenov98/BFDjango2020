from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticated

from core.models import ToDo, ToDoList, ToDoCategory, WorkToDo, StudyToDo
from core.serializers import ToDoSerializer, ToDoListSerializer, ToDoDetailedSerializer, StudyToDoSerializer, WorkToDoSerializer

import logging
logger = logging.getLogger(__name__)

class ToDoListViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    def get_queryset(self):
        return ToDoList.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)
        logger.info(f'To do list({serializer.instance}) is created!')
        logger.debug(f'To do list({serializer.instance}) is created!')

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

class ToDoViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = ToDo.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ToDoSerializer
        if self.action == 'retrieve':
            return ToDoDetailedSerializer

        return ToDoSerializer


class WorkToDoViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = WorkToDoSerializer

    def get_queryset(self):
        return ToDo.objects.filter(task=self.request.task)


class StudyToDoViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = StudyToDoSerializer

    def get_queryset(self):
        return ToDo.objects.filter(task=self.request.task)
