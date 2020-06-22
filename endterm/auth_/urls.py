from django.urls import path
from auth_ import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', views.MainUserViewSet, base_name="user")

urlpatterns = router.urls
