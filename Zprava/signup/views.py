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

def setting(request):
    new_username = request.GET.get('nusername')
    new_password = request.GET.get('npassword')
    username = request.GET.get('username')
    just_pass_change = False
    just_user_change = False
    no_change = False
    username_exist = False

    if username == new_username and not new_password == '':
        just_pass_change = True

    if new_password == '' and not username == new_username:
        just_user_change = True

    if new_username == username and new_password == '':
        no_change = True

    if no_change == True:
         return HttpResponse('NoChange')

    for user in Users.objects.all():
        if user.username == new_username:
            username_exist = True

    if new_username == '':
        return HttpResponse('Empty')
    if username_exist and not just_pass_change:
        return HttpResponse('Taken')

    if just_pass_change and not just_user_change :
        for user in Users.objects.all():
            if user.username == username:
                user.password = new_password
                user.save()
                return HttpResponse('Pass')
    elif just_user_change and not just_pass_change:
        for user in Users.objects.all():
            if user.username == username:
                user.username = new_username
                user.save()
                return HttpResponse('User')
    elif not just_pass_change and not just_user_change:
        for user in Users.objects.all():
            if user.username == username:
                user.username = new_username
                user.save()
                user.password = new_password
                user.save()
                return HttpResponse('PassUser')



