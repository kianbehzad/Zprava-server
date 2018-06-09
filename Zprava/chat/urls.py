from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "chat"

urlpatterns = [
    path('getchats/', views.getchats, name='getchats'),

]

urlpatterns = format_suffix_patterns(urlpatterns)