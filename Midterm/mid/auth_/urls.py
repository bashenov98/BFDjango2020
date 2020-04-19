from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from auth_.views import UserCreateView,UserViewSet

router = DefaultRouter()
router.register(r'register', UserViewSet)

urlpatterns = [
    path('login', obtain_jwt_token),
    path('', include(router.urls)),
]