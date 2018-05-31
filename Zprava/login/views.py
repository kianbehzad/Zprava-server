from django.shortcuts import render
from django.http import HttpResponse
from signup.models import Users

# Create your views here.

def login(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    if not username or not password:
        return HttpResponse("Incomplete")
    username_exist = False
    is_verified = False
    correct_password = False
    for user in Users.objects.all():
        if user.username == username:
            username_exist = True
            if user.is_verified:
                is_verified = True
            if user.password == password:
                correct_password = True

    if not username_exist:
        return HttpResponse("InvalidUsername")
    elif not is_verified:
        return HttpResponse("NotValidate")
    elif not correct_password:
        return HttpResponse("InvalidPassword")
    else:
        return HttpResponse("Enter")