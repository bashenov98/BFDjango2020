from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import BookViewSet, JournalViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'journals', JournalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]