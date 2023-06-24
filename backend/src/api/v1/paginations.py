from rest_framework.pagination import PageNumberPagination


class CommentsPagination(PageNumberPagination):
    """Пагинация комментариев"""
    page_size = 10
