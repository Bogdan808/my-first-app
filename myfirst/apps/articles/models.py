import datetime
from django.db import models
from django.utils import timezone

class Article(models.Model):
    article_title = models.CharField('название статьи', max_length=200)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    autor_name = models.CharField('имя автора', max_length=40)
    comment_text = models.CharField('текст комментария', max_length=200)

    def __str__(self):
        return self.autor_name

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
