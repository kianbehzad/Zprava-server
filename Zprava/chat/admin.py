from django.contrib import admin
from chat.models import Chat, TextMessage
# Register your models here.

admin.site.register(Chat)
admin.site.register(TextMessage)
