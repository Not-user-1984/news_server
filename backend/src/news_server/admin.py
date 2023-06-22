from django.contrib import admin

from .models import Comments, News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'date',
        'title',
        'text',
        'author',
        )
    search_fields = (
        'author',

        )
    list_fields = (
        'author',
        )


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'date',
        'text',
        'author',
        'news',
        )
    search_fields = (
        'news',

        )
    list_fields = (
        'news',
        )