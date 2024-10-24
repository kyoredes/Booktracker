from rest_framework import generics
from django.contrib.auth import get_user_model
from users.serializer import UserSeriazer


class UserListAPIView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSeriazer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSeriazer


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSeriazer


class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSeriazer


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSeriazer
