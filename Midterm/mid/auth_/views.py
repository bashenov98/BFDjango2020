from django.shortcuts import render

from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny

from auth_.models import CustomUser
from auth_.serializers import CustomUserSerializer

from rest_framework.permissions import IsAuthenticated
# Create your views here.

class UserCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    authentication_classes = ()

    def get_queryset(self):
        return CustomUser.objects.all()

    def get_serializer_class(self):
        return CustomUserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user)
        return CustomUser.objects.all()

    def get_serializer_class(self):
        return CustomUserSerializer

    def perform_create(self, serializer):
        serializer.save()