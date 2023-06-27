from news_server.models import Comments, News
from news_server.servis_likes import add_like, is_liked_by_user, remove_like
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .permissions import AllowAnyReadOnly, IsAdminOrReadOnly
from .serializers import CommentsSerializer, NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    """ViewSet для новостей"""
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AllowAnyReadOnly]

    def perform_create(self, serializer):
        """
        Метод создания новости.
        """
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        """
        Добавление лайка к новости.
        """
        news = self.get_object()
        if is_liked_by_user(news_id=news.id, user_id=request.user.id):
            return Response(
                {'error': 'вы уже поставили лайк'},
                status=status.HTTP_400_BAD_REQUEST)
        add_like(news_id=news.id, user_id=request.user.id)
        serializer = self.serializer_class(news)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        """
        Удаление лайка у новости.
        """
        news = self.get_object()
        if not is_liked_by_user(news_id=news.id, user_id=request.user.id):
            return Response(
                {'error': 'вы еще не поставили лайк'},
                status=status.HTTP_400_BAD_REQUEST)
        remove_like(news_id=news.id, user_id=request.user.id)
        serializer = self.serializer_class(news)
        return Response(serializer.data)

    def get_serializer_context(self):
        """
        Получение контекста сериализатора.
        """
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if user.is_staff or instance.author == user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {'error': "Вы не можете удалить эту новость"},
                status=status.HTTP_403_FORBIDDEN
                )


class CommentsViewSet(viewsets.ModelViewSet):
    """ViewSet для комментариев"""
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        """
        Метод создания комментария.
        """
        serializer.save(author=self.request.user)

    def get_queryset(self):
        """
        Получение списка комментариев.
        """
        news_id = self.request.query_params.get('news_id')
        queryset = Comments.objects.filter(
            news=news_id) if news_id else Comments.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        """
        Создание комментария.
        """
        if not request.user.is_authenticated:
            return Response(
                {'error': 'недостаточно прав для создания комментария'},
                status=status.HTTP_403_FORBIDDEN
                )

        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удаление комментария.
        """
        instance = self.get_object()
        if request.user.is_admin or instance.author == request.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(
            {'error': 'недостаточно прав для удаления'},
            status=status.HTTP_403_FORBIDDEN
            )
