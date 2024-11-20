from rest_framework import serializers
from booklists.models import Booklist
from users.serializers import UserSerializer


class BooklistSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Booklist
        fields = '__all__'
