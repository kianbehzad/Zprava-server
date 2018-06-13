from django.shortcuts import render
from django.http import HttpResponse
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
    is_exist = False
    for _user in Users.objects.all():
        if _user.username == username:
            is_exist = True
            user = _user
    if not is_exist:
        return HttpResponse('NotExist')
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

def textmessage(request):
    publisher = request.GET.get("publisher")
    subscriber = request.GET.get("subscriber")
    textmessage = request.GET.get("textmessage")
    user_publisher = None
    user_subscriber = None
    is_publisher_exist = False
    is_subscriber_exists = False
    for _user in Users.objects.all():
        if _user.username == publisher:
            is_publisher_exist = True
            user_publisher = _user
        if _user.username == subscriber:
            is_subscriber_exists = True
            user_subscriber = _user
    if not is_publisher_exist and not is_publisher_exist:
        return HttpResponse('NoPublisherSubscriber')
    if not is_publisher_exist:
        return HttpResponse('NoPublisher')
    if not is_subscriber_exists:
        return HttpResponse('NoSubscriber')
    chat = None
    chat_exist = False
    for _chat in Chat.objects.all():
        if user_publisher == _chat.first_side and user_subscriber == _chat.second_side:
            chat = _chat
            chat_exist = True
        elif user_publisher == _chat.second_side and user_subscriber == _chat.first_side:
            chat = _chat
            chat_exist = True


    if not chat_exist:
        chat = Chat(first_side=user_publisher, second_side=user_subscriber)
        chat.save()
    textmessage = TextMessage(publisher = user_publisher, subscriber = user_subscriber, chat = chat, text = textmessage)
    textmessage.save()
    return HttpResponse("TextMessageCreated")















