# Generated by Django 2.0.5 on 2018-07-08 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0014_textmessage_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='textmessage',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
