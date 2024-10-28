from rest_framework import serializers
from django.contrib.auth import get_user_model
from books.models import Book


class UserSerializer(serializers.HyperlinkedModelSerializer):
    booklist = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(),
        many=True,
    )

    class Meta:
        model = get_user_model()
        fields = '__all__'
