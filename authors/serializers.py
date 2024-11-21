from authors.models import Author
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'
