from news_server.models import Comments, News
from rest_framework import status, viewsets
from rest_framework.response import Response
from news_server.servis_likes import add_like, remove_like, is_liked_by_user
from .permissions import IsAuthorOrAdminOrReadOnly
from .serializers import CommentsSerializer, NewsSerializer
from rest_framework.decorators import action


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthorOrAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        news = self.get_object()
        if is_liked_by_user(news_id=news.id, user_id=request.user.id):
            return Response(
                {'error': 'вы уже постали лайк'},
                status=status.HTTP_400_BAD_REQUEST)

        add_like(news_id=news.id, user_id=request.user.id)
        serializer = self.serializer_class(news)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        news = self.get_object()
        if not is_liked_by_user(news_id=news.id, user_id=request.user.id):
            return Response(
                {'error': 'нет вашего лайка'},
                status=status.HTTP_400_BAD_REQUEST)
        remove_like(news_id=news.id, user_id=request.user.id)
        serializer = self.serializer_class(news)
        return Response(serializer.data)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthorOrAdminOrReadOnly]

    def get_queryset(self):
        news_id = self.kwargs['news_id']
        return Comments.objects.filter(news=news_id)

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            news_id=self.kwargs['news_id'])

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.is_admin or instance.author == request.user:
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.is_admin or instance.author == request.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def get_comment(self, comment_id):
        comment = Comments.objects.get(id=comment_id)
        comment.liked_by_user = is_liked_by_user(comment_id=comment_id, user_id=self.request.user.id)
        return comment

    @action(detail=True, methods=['post'])
    def add_like(self, request, pk=None):
        comment = self.get_object()
        user_id = request.user.id
        add_like(comment_id=comment.id, user_id=user_id)
        comment.liked_by_user = True
        serializer = self.get_serializer(comment)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def remove_like(self, request, pk=None):
        comment = self.get_object()
        user_id = request.user.id
        remove_like(comment_id=comment.id, user_id=user_id)
        comment.liked_by_user = False
        serializer = self.get_serializer(comment)
        return Response(serializer.data)