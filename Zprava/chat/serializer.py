from rest_framework import serializers
from.models import TextMessage
from signup.serializer import UsersSerializer


class TextMessageSerializer(serializers.ModelSerializer):
    publisher = UsersSerializer()
    subscriber = UsersSerializer()

    class Meta:
        model = TextMessage
        fields = ['publisher', 'subscriber', 'datetime', 'is_seen', 'text']