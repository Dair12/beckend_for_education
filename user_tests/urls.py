from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserTestViewSet

router = DefaultRouter()
router.register(r'', UserTestViewSet, basename='user-tests')

urlpatterns = [
    path('', include(router.urls)),
]