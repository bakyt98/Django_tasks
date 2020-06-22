from django.urls import path
from core import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', views.ArticleViewSet, base_name="articles")
# router.register('articles', views.ArticleListViewSet, base_name='articles')
# router.register('favorites', views.FavoriteArticleViewSet, base_name='favorite-articles')

urlpatterns = router.urls
