from django.db import models
from signup.models import Users


# Create your models here.

class Chat(models.Model):
    first_side = models.ForeignKey(Users, related_name="first_chat_set", null=True,on_delete=models.SET_NULL)
    second_side = models.ForeignKey(Users, related_name="second_chat_set", null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_side.username + ' - ' + self.second_side.username


class TextMessage(models.Model):
    publisher = models.ForeignKey(Users, related_name="sender_textmessage_set", null=True, on_delete=models.SET_NULL)
    subscriber = models.ForeignKey(Users, related_name="receiver_textmessage_set", null=True, on_delete=models.SET_NULL)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.publisher.username + ' - ' + self.subscriber.username + ' : ' + self.text[0:20] + '...'
