from rest_framework import serializers
from.models import TextMessage
from signup.models import Users
from signup.serializer import UsersSerializer


class TextMessageSerializer(serializers.ModelSerializer):
    publisher = serializers.StringRelatedField()
    subscriber = serializers.StringRelatedField()
    origin_publisher = serializers.StringRelatedField()

    class Meta:
        model = TextMessage
        fields = ['publisher', 'subscriber', 'origin_publisher', 'is_forward', 'datetime', 'is_seen', 'text', 'type', 'pk']