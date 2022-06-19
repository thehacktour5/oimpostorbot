# Generated by Django 3.2.7 on 2022-06-19 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20211024_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='points',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='username',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(default='', max_length=100, verbose_name='Email'),
        ),
    ]
