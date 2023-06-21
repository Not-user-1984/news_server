from rest_framework import viewsets, permissions
from news_server.models import Comments, News
from .serializers import NewsSerializer, CommentsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        news_id = self.kwargs['news_id']
        return Comments.objects.filter(news=news_id)

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            news_id=self.kwargs['news_id'])
