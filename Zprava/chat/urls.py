from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "chat"

urlpatterns = [
    path('getchats/', views.getchats, name='getchats'),
    path('textmessage/', views.textmessage, name='textmessage'),
]

urlpatterns = format_suffix_patterns(urlpatterns)