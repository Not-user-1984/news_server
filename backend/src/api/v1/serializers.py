from rest_framework import serializers
from users.serializers import UserSerializer
from news_server.models import News, Comments


class NewsSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = News
        fields = ['id', 'date', 'title', 'text', 'author']


class CommentsSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    news_title = serializers.CharField(source='news.title', read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'date', 'text', 'author', 'news', 'news_title']
