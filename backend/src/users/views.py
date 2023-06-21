from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from users.serializers import UserSerializer
User = get_user_model()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    search_fields = ('=username',)
    serializer_class = UserSerializer
