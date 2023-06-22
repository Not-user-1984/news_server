from django.contrib import admin


from .models import User


@admin.register(User)
class AdminCustomUser(admin.ModelAdmin):
    """
    Для модели пользователей включена фильтрация по имени и email
    """
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        )
    search_fields = (
        'username',
        )
    list_fields = (
        'username',
        )
