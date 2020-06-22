from django.db import models
from django.conf import settings
from utils import constants, file_utils


class Article(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    price = models.PositiveIntegerField(default=0)
    city = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=constants.CATEGORIES,
                                default=constants.CATEGORY1)
    color = models.CharField(max_length=100, choices=constants.COLORS,
                             default=constants.BLACK)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                related_name='articles')

    def __str__(self):
        return f'{self.name} - {self.creator}'


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images', validators=[
        file_utils.validate_image_extension, file_utils.validate_image_size])

    def __str__(self):
        return self.article


class FavoriteArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='users')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='favorite_articles')

    def __str__(self):
        return f'{self.user}: {self.article}'
