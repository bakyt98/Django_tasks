from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import ArticleSerializer, FavoriteArticleSerializer, AddFavorite
from .models import Article, FavoriteArticle


class ArticleViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get_queryset(self):
        if self.action != 'list':
            return self.queryset.filter(creator=self.request.user)
        return self.queryset

    def get_serializer_class(self):
        if self.action == 'favorite':
            return FavoriteArticleSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    @action(methods=['POST'], detail=False)
    def favorite(self, request):
        serializer = AddFavorite(data=request.data)
        serializer.is_valid(raise_exception=True)
        fav = serializer.add_favorite(self.request.user)
        return Response(ArticleSerializer(fav).data)

    @action(methods=['GET'], detail=False)
    def favorite_list(self, request):
        articles = FavoriteArticle.objects.filter(user=self.request.user)
        serializer = FavoriteArticleSerializer(articles, many=True)
        return Response(serializer.data)



class ArticleListViewSet(viewsets.generics.ListAPIView, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


# class FavoriteArticleViewSet(mixins.CreateModelMixin,
#                              viewsets.generics.ListAPIView,
#                              viewsets.GenericViewSet):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = FavoriteArticleSerializer
#     queryset = FavoriteArticle.objects.all()

#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
