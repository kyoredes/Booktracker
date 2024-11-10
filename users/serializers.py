from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = get_user_model()
        fields = ['username', 'password']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    booklist = serializers.HyperlinkedRelatedField(
        read_only=True,
        many=True,
        view_name='booklist-detail',
    )

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'booklist']
