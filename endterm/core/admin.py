from django.contrib import admin
from .models import ArticleImage, Article, FavoriteArticle


admin.site.register(Article)
admin.site.register(ArticleImage)
admin.site.register(FavoriteArticle)
