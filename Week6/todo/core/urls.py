from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views.views import ToDoListAPIView, ToDoListDetailAPIView, ToDoAPIView
from core.views.viewsets import ToDoListViewSet

router = DefaultRouter()
router.register(r'favorites', ToDoListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("todolists/", ToDoListAPIView.as_view()),
    path("todolists/<int:id>/", ToDoListDetailAPIView.as_view()),
    path("todolists/<int:id>/todo/", ToDoAPIView.as_view())
]