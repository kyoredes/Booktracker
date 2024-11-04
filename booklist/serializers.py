from rest_framework import serializers
from booklist.models import Booklist
from users.serializers import UserSerializer


class BooklistSerializer(serializers.HyperlinkedModelSerializer):
    username = UserSerializer(many=True)

    class Meta:
        model = Booklist
        fields = '__all__'
