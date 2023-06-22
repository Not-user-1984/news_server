from rest_framework import serializers
from news_server.models import News, Comments
from news_server.servis_likes import get_likes_count


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    comments = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(default=0, read_only=True)

    def get_comments(self, obj):
        queryset = Comments.objects.filter(news_id=obj)
        return CommentsSerializer(queryset, many=True).data

    def get_likes(self, obj):
        return get_likes_count(news_id=obj.id)

    class Meta:
        model = News
        fields = ['id', 'date', 'title', 'text', 'author', 'comments', 'likes']


class CommentsSerializer(serializers.ModelSerializer):
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
        if Comments.objects.filter(
            news_id=news_id,
            author=user,
            text=data['text']).exists():
            raise serializers.ValidationError("Этот комментарий уже существует.")
        return data
