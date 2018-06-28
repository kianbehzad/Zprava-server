from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "chat"

urlpatterns = [
    path('getallchats/', views.getallchats, name='getallchats'),
    path('getnewchats/', views.getnewchats, name='getnewchats'),
    path('newtextmessage/', views.newtextmessage, name='newtextmessage'),
    path('seen/', views.seen, name='seen'),
]

urlpatterns = format_suffix_patterns(urlpatterns)