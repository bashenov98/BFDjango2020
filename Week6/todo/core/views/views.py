from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.response import Response

from core.models import ToDoList, ToDo
from core.serializers import ToDoListSerializer, ToDoSerializer


class ToDoListAPIView(generics.ListCreateAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer


class ToDoListDetailAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ToDoAPIView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    lookup_field = "id"
