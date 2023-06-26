from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound


class CommentsPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100
    page_query_param = 'page'

    def paginate_queryset(self, queryset, request, view=None):
        """
        Переопределяемэтот метод
        для проверки допустимости
        номера запрашиваемой страницы.
        """
        try:
            return super().paginate_queryset(queryset, request, view=view)
        except NotFound as exc:
            # генерируем исключение, если номер страницы недействительный
            invalid_page = request.query_params.get(self.page_query_param)
            raise NotFound(f"Страница {invalid_page} не найдена.") from exc


class CustomPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 100
    page_query_param = 'page'

    def paginate_queryset(self, queryset, request, view=None):
        """
        Переопределяем этот метод
        для проверки допустимости
        номера запрашиваемой страницы.
        """
        try:
            return super().paginate_queryset(queryset, request, view=view)
        except NotFound as exc:
            # генерируем исключение, если номер страницы недействительный
            invalid_page = request.query_params.get(self.page_query_param)
            raise NotFound(f"Страница {invalid_page} не найдена.") from exc
