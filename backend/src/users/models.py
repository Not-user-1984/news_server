from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


ADMIN = 'admin'
USER = 'user'

ROLE_CHOICES = (
    (ADMIN, 'Администратор'),
    (USER, 'Пользователь')
)


class User(AbstractUser):
    """Модель пользователя"""
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        max_length=settings.LIMIT_EMAIL,
        help_text="Электронная почта пользователя"
    )
    username = models.CharField(
        verbose_name='Логин',
        max_length=settings.LIMIT_USERNAME,
        unique=True,
        help_text="Логин пользователя"
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=settings.LIMIT_USERNAME,
        help_text="Имя пользователя",
        blank=True
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=settings.LIMIT_USERNAME,
        help_text="Фамилия пользователя",
        blank=True
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=50,
        choices=ROLE_CHOICES,
        default=USER,
        help_text="Роль пользователя"
    )

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return str(self.username)

    @property
    def is_admin(self):
        """Проверка на администратора"""
        return self.role == ADMIN

    @property
    def is_user(self):
        """Проверка на пользователя"""
        return self.role == USER
