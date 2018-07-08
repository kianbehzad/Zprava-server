from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Chat, TextMessage
from .serializer import TextMessageSerializer
from signup.models import Users
from rest_framework.decorators import api_view
import datetime


# Create your views here.

##http://127.0.0.1:8000/chat/getallchats/?username=amirbayat98
@api_view(['GET', 'POST', ])
def getallchats(request):
    username = request.GET.get("username")
    user = None
    is_exist = False
    for _user in Users.objects.all():
        if _user.username == username:
            is_exist = True
            user = _user
    if not is_exist:
        return HttpResponse('InvalidUserName')
    data = {}
    has_any_message = False
    for chat in user.second_side_chats.all():
        dict = {}
        for x in chat.chat_text_messages.all():
            serializer = TextMessageSerializer(x, many=False)
            dict[x.pk] = serializer.data
        data[chat.first_side.username] = dict
        has_any_message = True
    for chat in user.first_side_chats.all():
        dict = {}
        for x in chat.chat_text_messages.all():
            serializer = TextMessageSerializer(x, many=False)
            dict[x.pk] = serializer.data
        data[chat.first_side.username] = dict
        has_any_message = True
    if not has_any_message:
        return HttpResponse('EmptyMessages')
    return Response(data)


@api_view(['GET', 'POST', ])
def getnewchats(request):
    username = request.GET.get("username")
    user = None
    is_exist = False
    for _user in Users.objects.all():
        if _user.username == username:
            is_exist = True
            user = _user
    if not is_exist:
        return HttpResponse('InvalidUserName')
    data = {}
    has_any_message = False
    has_new_message = False
    for chat in user.second_side_chats.all():
        new_messages = []
        for message in chat.chat_text_messages.all():
            if not message.is_seen:
                has_new_message = True
                new_messages.append(message)
        if has_new_message:
            dict = {}
            for x in new_messages:
                serializer = TextMessageSerializer(x, many=False)
                dict[x.pk] = serializer.data
            data[chat.first_side.username] = dict
        has_any_message = True
    for chat in user.first_side_chats.all():
        new_messages = []
        for message in chat.chat_text_messages.all():
            if not message.is_seen:
                has_new_message = True
                new_messages.append(message)
        if has_new_message:
            dict = {}
            for x in new_messages:
                serializer = TextMessageSerializer(x, many=False)
                dict[x.pk] = serializer.data
            data[chat.first_side.username] = dict
        has_any_message = True
    if not has_any_message:
        return HttpResponse('EmptyMessages')
    if not has_new_message:
        return HttpResponse('NoNewMessages')
    return Response(data)


##http://127.0.0.1:8000/chat/newtextmessage/?publisher=bn.warcraft&subscriber=amirbayat98&textmessage=new+msg
def newtextmessage(request):
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
        return HttpResponse('InvalidPublisherSubscriber')
    if not is_publisher_exist:
        return HttpResponse('InvalidPublisher')
    if not is_subscriber_exists:
        return HttpResponse('InvalidSubscriber')
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
    textmessage = TextMessage(publisher = user_publisher, subscriber = user_subscriber, chat = chat, text = textmessage, is_seen = False, datetime = datetime.datetime.now(), type="TEXT")
    user_publisher.last_message_datetime = textmessage.datetime
    textmessage.save()
    user_publisher.save()
    return HttpResponse("TextMessageCreated")



##http://127.0.0.1:8000/chat/seen/?whoami=amirbayat98&secondside=bn.warcraft
def seen(request):
    whoami = request.GET.get("whoami")
    secondside = request.GET.get("secondside")
    chat = None
    is_chat_exists = False
    for _chat in Chat.objects.all():
        if _chat.first_side.username == whoami and _chat.second_side.username == secondside:
            chat = _chat
            is_chat_exists = True
        if _chat.first_side.username == secondside and _chat.second_side.username == whoami:
            chat = _chat
            is_chat_exists = True
    if not is_chat_exists:
        return HttpResponse('InvalidChat')
    ##else
    for textmessage in chat.chat_text_messages.all():
        if textmessage.publisher.username == secondside:
            textmessage.is_seen = True
            textmessage.save()
    return HttpResponse('Seen')











