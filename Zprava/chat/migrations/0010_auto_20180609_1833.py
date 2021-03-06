# Generated by Django 2.0.5 on 2018-06-09 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_auto_20180609_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='first_side',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='first_set', to='signup.Users'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='second_side',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_set', to='signup.Users'),
        ),
        migrations.AlterField(
            model_name='textmessage',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sender_set', to='signup.Users'),
        ),
        migrations.AlterField(
            model_name='textmessage',
            name='subscriber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receiver_set', to='signup.Users'),
        ),
    ]
