# Generated by Django 2.0.5 on 2018-06-08 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
        ('chat', '0004_auto_20180608_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='textmessage',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender_user', to='signup.Users'),
        ),
        migrations.AddField(
            model_name='textmessage',
            name='subscriber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver_user', to='signup.Users'),
        ),
    ]