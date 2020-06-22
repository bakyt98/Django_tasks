from .models import Article, ArticleImage, FavoriteArticle
from auth_.serializers import MainUserSerializer
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('creator',)


class FullArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('creator',)


class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = '__all__'


class AddFavorite(serializers.Serializer):
    article_id = serializers.IntegerField()


    def add_favorite(self, user):
        fav = FavoriteArticle.objects.create(article_id=self.validated_data['article_id'], user=user)
        return fav.article


class FavoriteArticleSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()
    user = MainUserSerializer()
    class Meta:
        model = FavoriteArticle
        fields = '__all__'
        read_only_fields = ('user',)
