from rest_framework import viewsets
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer


class UserAPIViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
