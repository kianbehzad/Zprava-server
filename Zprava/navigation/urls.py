from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "navigation"

urlpatterns = [
    path('userdata/', views.userdata, name='userdata'),
]

urlpatterns = format_suffix_patterns(urlpatterns)