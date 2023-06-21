
from django.db import models
from users.models import User


class News(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comments(models.Model):
    date = models.DateField(auto_now_add=True)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

