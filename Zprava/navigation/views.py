from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from signup.models import Users
from signup.serializer import UsersSerializer
from rest_framework.decorators import api_view

# Create your views here.



@api_view(['GET', 'POST', ])
def userdata(request):
    username = request.GET.get("username")
    user = None
    is_exist = False
    for _user in Users.objects.all():
        if _user.username == username:
            is_exist = True
            user = _user
    if not is_exist:
        return HttpResponse('InvalidUserName')
    ##else
    serializer = UsersSerializer(user)
    return Response(serializer.data)
