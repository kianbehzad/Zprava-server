from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Users
import random

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
        user = Users(username=username, password=password, email=email, verification_code=verification_code, is_verified=False)
        send_mail(
            'Zprava Verification Code',
            'you Zprava verification code is: '+ str(verification_code),
            'kian.behzad@gmail.com',
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

def forget(request):
    email = request.GET.get("email")
    if not email:
        return HttpResponse("Incomplete")
    email_exist = False
    for user in Users.objects.all():
        if user.email == email:
            send_mail(
                'Zprava Restore Your Data',
                'your Zprava username is: ' + user.username + '    -    and your password is: ' + user.password,
                'kian.behzad@gmail.com',
                [user.email],
                fail_silently=True,
            )
            email_exist = True
    if not email_exist:
        return HttpResponse("InvalidEmail")
    else:
        return HttpResponse("Sent")

