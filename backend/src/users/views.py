# from django.contrib.auth import get_user_model
# from rest_framework.viewsets import ModelViewSet
# from users.serializers import UserSerializer
# from api.v1.permissions import IsAdminOrReadOnly,IsAuthorOrAdminOrReadOnly
# User = get_user_model()


# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     search_fields = ('=username',)
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthorOrAdminOrReadOnly]
