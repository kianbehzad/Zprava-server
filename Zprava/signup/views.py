from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Users
import random
import datetime


# Create your views here.

def registration(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    email = request.GET.get("email")
    if not username or not password or not email:
        return HttpResponse("Incomplete")
    username_exist = False
    email_exist = False
    for user in Users.objects.all():
        if user.username == username:
            username_exist = True
        if user.email == email:
            email_exist = True
    if username_exist and email_exist:
        return HttpResponse("BothExist")
    elif username_exist:
        return HttpResponse("UsernameExist")
    elif email_exist:
        return HttpResponse("EmailExist")
    else:
        verification_code = random.randint(10000, 99999)
        user = Users(username=username, password=password, email=email, verification_code=verification_code, is_verified=False, last_message_datetime=datetime.datetime.now())
        send_mail(
            'Zprava Verification Code',
            'you Zprava verification code is: '+ str(verification_code),
            'community@zprava.ir',
            [user.email],
            fail_silently=True,
        )
        user.save()
        return HttpResponse("pre_verified")

def hello(request):
    return HttpResponse("hello back")

def verification(request):
    username = request.GET.get("username")
    verification_code = request.GET.get("verification_code")
    if not username or not verification_code:
        return HttpResponse("Incomplete")
    username_exist = False
    is_code_correct = False
    for user in Users.objects.all():
        if user.username == username:
            username_exist = True
            if user.verification_code == verification_code:
                user.is_verified = True
                user.save()
                is_code_correct = True
    if not username_exist:
        return HttpResponse("InvalidUsername")
    elif not is_code_correct:
        return HttpResponse("InvalidCode")
    else:
        return HttpResponse("Enter")


def changeusername(request):
    old_username = request.GET.get("old_username")
    new_username = request.GET.get("new_username")
    old_username_exist = False
    old_user = None
    for user in Users.objects.all():
        if user.username == old_username:
            old_username_exist = True
            old_user = user
    for user in Users.objects.all():
        if user.username == new_username:
            return HttpResponse("UsernameTaken")
    if not old_username_exist:
        return HttpResponse("InvalidUsername")

    old_user.username = new_username
    old_user.save()
    return HttpResponse("UsernameChanged")



def changepassword(request):
    username = request.GET.get("username")
    old_password = request.GET.get("old_password")
    new_password = request.GET.get("new_password")
    username_exist = False
    user = None
    for _user in Users.objects.all():
        if _user.username == username:
            username_exist = True
            user = _user
    if not username_exist:
        return HttpResponse("InvalidUsername")
    if not user.password == old_password:
        return HttpResponse("IncorrectPassword")
    user.password = new_password
    user.save()
    return HttpResponse("PasswordChanged")