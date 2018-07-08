from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    verification_code = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=False)
    last_message_datetime = models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username