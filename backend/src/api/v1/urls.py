from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import NewsViewSet, CommentsViewSet


app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register(
    prefix='news',
    viewset=NewsViewSet, basename='news'
    )
router_v1.register(
    r'news/(?P<news_id>\d+)/comments',
    viewset=CommentsViewSet,
    basename='comments'
    )

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
