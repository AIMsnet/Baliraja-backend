# Generated by Django 3.0.6 on 2020-05-12 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aimsBaliraja', '0002_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]