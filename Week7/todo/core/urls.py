from rest_framework.routers import DefaultRouter
from django.urls import path, include

from core.views.views import ToDoAPIView, ToDoListDetailAPIView, ToDoListAPIView
from core.views.viewsets import WorkToDoViewSet, ToDoViewSet, StudyToDoViewSet, ToDoListViewSet

router = DefaultRouter()

router.register(r'works', WorkToDoViewSet, basename="core")
router.register(r'studies', StudyToDoViewSet, basename="core")
router.register(r'todoo', ToDoViewSet, basename="core")
router.register(r'todoolist', ToDoListViewSet, basename="core")

urlpatterns = [
    path('', include(router.urls)),
    path("todolists/", ToDoListAPIView.as_view()),
    path("todolists/<int:id>/", ToDoListDetailAPIView.as_view()),
    path("todolists/<int:id>/todo/", ToDoAPIView.as_view())
]