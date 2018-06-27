from django.db import models
from signup.models import Users


# Create your models here.

class Chat(models.Model):
    first_side = models.ForeignKey(Users, related_name="first_side_chats", null=True, on_delete=models.CASCADE)
    second_side = models.ForeignKey(Users, related_name="second_side_chats", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_side.__str__() + ' - ' + self.second_side.__str__()


class TextMessage(models.Model):
    publisher = models.ForeignKey(Users, related_name="published_text_messages", null=True, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(Users, related_name="subscribed_text_messages", null=True, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, related_name="chat_text_messages", null=True, on_delete=models.CASCADE)
    is_seen = models.BooleanField(default=False)
    datetime = models.CharField(max_length=50, null=True)
    text = models.CharField(max_length=1000)


    def __str__(self):
        return self.publisher.__str__() + ' - ' + self.subscriber.__str__() + ' : ' + self.text[0:20] + '...'