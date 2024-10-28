from authors.models import Author
from books.models import Book
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(),
        many=True,
    )

    class Meta:
        model = Author
        fields = '__all__'
