from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Chat, TextMessage
from .serializer import TextMessageSerializer
from signup.models import Users
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET', 'POST', ])
def getchats(request):
    username = request.GET.get("username")
    user = None
    for _user in Users.objects.all():
        if _user.username == username:
            user = _user
    #user1.second_set.all()[0].textmessage_set.all()
    data = {}
    for chat in user.second_chat_set.all():
            serializer = TextMessageSerializer(chat.textmessage_set.all(), many=True)
            data[chat.first_side.username] = serializer.data
    for chat in user.first_chat_set.all():
            serializer = TextMessageSerializer(chat.textmessage_set.all(), many=True)
            data[chat.second_side.username] = serializer.data

    #user_send_messages = Users.objects.all()[0].sender_textmessage_set.all()
    #serializer = TextMessageSerializer(user_send_messages, many=True)
    return Response(data)