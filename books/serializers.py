from rest_framework import serializers
from books.models import Book
from authors.serializers import AuthorSerializer


class BookSerializer(serializers.HyperlinkedModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
