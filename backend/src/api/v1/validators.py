from news_server.models import News, Comments
from rest_framework import serializers


def validate_news_title(title):
    if News.objects.filter(title=title).exists():
        raise serializers.ValidationError(
            "Новость с таким заголовком уже существует."
        )


def validate_news_text(text):
    if News.objects.filter(text=text).exists():
        raise serializers.ValidationError(
            "Новость с таким содержанием уже существует."
        )


def validate_comment(news_id, author, text):
    if Comments.objects.filter(
            news_id=news_id,
            author=author,
            text=text
        ).exists():
        raise serializers.ValidationError(
            "Этот комментарий уже существует."
        )
