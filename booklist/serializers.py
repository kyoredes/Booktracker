from rest_framework import serializers
from booklist.models import Readlist


class BooklistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Readlist
        fields = '__all__'
