from django.db import models
from users.models import User


class News(models.Model):
    """Модель новости"""
    date = models.DateField(
        auto_now_add=True,
        help_text="Дата создания новости"
    )
    title = models.CharField(
        max_length=255,
        help_text="Заголовок новости"
    )
    text = models.TextField(
        help_text="Текст новости"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Автор новости"
    )

    def __str__(self):
        return str(self.author)

    class Meta:
        ordering = ['date']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comments(models.Model):
    """Модель комментария к новости"""
    date = models.DateField(
        auto_now_add=True,
        help_text="Дата создания комментария"
    )
    text = models.TextField(
        help_text="Текст комментария"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Автор комментария"
    )
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        help_text="Ссылка на новость, к которой написан комментарий"
    )

    def __str__(self):
        return str(self.author)

    class Meta:
        ordering = ['date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
