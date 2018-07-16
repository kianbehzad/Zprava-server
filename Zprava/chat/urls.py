from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "chat"

urlpatterns = [
    path('getallchats/', views.getallchats, name='getallchats'),
    path('getnewchats/', views.getnewchats, name='getnewchats'),
    path('newtextmessage/', views.newtextmessage, name='newtextmessage'),
    path('seen/', views.seen, name='seen'),
    path('deletemessage/', views.deletemessage, name='deletemessage'),
    ##new approach
    path('getmessage/', views.getmessage, name='getmessage'),
    path('chatheaders/', views.chatheaders, name='chatheaders'),
]

urlpatterns = format_suffix_patterns(urlpatterns)