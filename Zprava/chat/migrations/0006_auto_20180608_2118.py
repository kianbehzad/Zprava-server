# Generated by Django 2.0.5 on 2018-06-08 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20180608_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textmessage',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sender_user', to='signup.Users'),
        ),
        migrations.AlterField(
            model_name='textmessage',
            name='subscriber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receiver_user', to='signup.Users'),
        ),
    ]