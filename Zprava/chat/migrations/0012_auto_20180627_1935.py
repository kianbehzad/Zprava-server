# Generated by Django 2.0.5 on 2018-06-27 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
        ('chat', '0011_auto_20180609_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('datetime', models.CharField(max_length=50)),
                ('is_seen', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='textmessage',
            name='chat',
        ),
        migrations.RemoveField(
            model_name='textmessage',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='textmessage',
            name='subscriber',
        ),
        migrations.AlterField(
            model_name='chat',
            name='first_side',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_side_chats', to='signup.Users'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='second_side',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_side_chats', to='signup.Users'),
        ),
        migrations.AddField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages', to='chat.Chat'),
        ),
        migrations.AddField(
            model_name='message',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='published_messages', to='signup.Users'),
        ),
        migrations.AddField(
            model_name='message',
            name='subscriber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscribed_messages', to='signup.Users'),
        ),
        migrations.AddField(
            model_name='textmessage',
            name='base',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_messages', to='chat.Message'),
        ),
    ]