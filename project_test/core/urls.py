from django.urls import path
from .views import create_user, get_all_users, CarViewSet, CarViewSet3
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('create_user/', create_user),
    path('get_users/', get_all_users),
]

router = DefaultRouter()

router.register('cars', CarViewSet, basename="cars")
router.register('cars2', CarViewSet3, basename='cars2')

urlpatterns += router.urls
