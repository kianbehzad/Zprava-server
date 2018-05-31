from django.urls import path
from . import views

app_name = "signup"

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('hello/', views.hello, name='hello'),
]