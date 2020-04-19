from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics, mixins

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from core.serializers import BookSerializer, JournalSerializer

from rest_framework.response import Response
from rest_framework.decorators import action




from core.models import Book, Journal
# Create your views here.
class BookViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        return BookSerializer

    def perform_create(self, serializer):
        serializer.save()


class JournalViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Journal.objects.all()

    def get_serializer_class(self):
        return JournalSerializer

    def perform_create(self, serializer):
        serializer.save()

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = (IsAuthenticated )
#
#     def perform_create(self, serializer):
#         serializer.save()
#
#
# class JournalViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = JournalSerializer
#     permission_classes = (IsAuthenticated, )
#
#     def perform_create(self, serializer):
#         serializer.save()

