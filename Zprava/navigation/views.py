from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from signup.models import Users
from signup.serializer import UsersSerializer
from rest_framework.decorators import api_view
import re

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

@api_view(['GET', 'POST', ])
def search(request):
    searched_word = request.GET.get("word")
    parts_of_searched_word = []
    patterns_of_searched_words = []
    matched_users = []
    string_result =''
    flag = 0

    parts_of_searched_word = re.split(r'; |, |\*|\n|_|\.|@|!|#|\$|%|\^|&|\(|-\)|\+|=|"|;|:|<|>|\?|~', searched_word)

    for word in parts_of_searched_word:
        patterns_of_searched_words.append(re.compile(word))


    for user in Users.objects.all():
        if searched_word == user.username:
            string_result = user.username
            flag = 1
        else:
            continue

    for word_pat in patterns_of_searched_words:
        for user in Users.objects.all():
            if re.search(word_pat, user.username) != None and user.username not in matched_users:
                matched_users.append(user.username)
                flag = 2

    if flag == 2:
        string_result = '~'.join(matched_users)
    elif flag == 0:
        string_result = 'No Match Found'


    return HttpResponse(string_result)




