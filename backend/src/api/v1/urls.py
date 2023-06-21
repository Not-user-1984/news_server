from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import NewsViewSet, CommentsViewSet
from users.views import UserViewSet

app_name = 'users'

router_v1 = DefaultRouter()
router_v1.register(prefix='news', viewset=NewsViewSet,basename='news')
router_v1.register(prefix='comment', viewset=CommentsViewSet, basename='comment')
router_v1.register(prefix='users', viewset=UserViewSet, basename='users')
urlpatterns = [
    path('', include(router_v1.urls)),
]