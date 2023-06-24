from django.contrib import admin


from .models import User


@admin.register(User)
class AdminCustomUser(admin.ModelAdmin):
    """
    Для модели пользователей включена фильтрация по имени и email
    """
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональная информация', {
            'fields': ('first_name', 'last_name',)
        }),
        ('Права', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'role',
                'groups',
                'user_permissions',
            )
        }),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'role',
        'id',
    )
    list_editable = (
        'role',
    )
    search_fields = (
        'email',
        'first_name',
        'last_name',
        'username',
    )
    ordering = ('email', 'first_name', '-id', 'last_name', 'username',)
