from rest_framework import serializers
from booklists.models import Booklist


class BooklistSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Booklist
        fields = '__all__'
