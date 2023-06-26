from api.v1.validators import (validate_comment, validate_news_text,
                               validate_news_title)
from django.conf import settings
from news_server.models import Comments, News
from news_server.servis_likes import get_likes_count
from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
    """NewsSerializer осуществляет сериализацию объектов News модели"""
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    comments = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(default=0, read_only=True)

    def get_comments(self, obj):
        queryset = Comments.objects.filter(news_id=obj)[:settings.LIMIT_COMMIT]
        return CommentsSerializer(queryset, many=True).data

    def get_likes(self, obj):
        return get_likes_count(news_id=obj.id)

    def validate(self, data):
        title = data.get('title')
        text = data.get('text')
        validate_news_title(title)
        validate_news_text(text)
        return data

    class Meta:
        model = News
        fields = ['id', 'date', 'title', 'text', 'author', 'comments', 'likes']


class CommentsSerializer(serializers.ModelSerializer):
    """CommentsSerializer осуществляет сериализацию
    объектов Comments модели."""
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    news_title = serializers.CharField(source='news.title', read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'date', 'text', 'author', 'news', 'news_title']

    def validate(self, data):
        news_id = self.context['view'].kwargs.get('news_id')
        user = self.context['request'].user
        validate_comment(news_id, user, data['text'])
        return data
