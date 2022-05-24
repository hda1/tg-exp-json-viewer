from django.db import models

class User(models.Model):
    user = models.CharField(max_length=35, verbose_name='Пользователь')
    user_id = models.CharField(max_length=35, verbose_name='ID')

class Chat(models.Model):
    id = models.IntegerField(editable=False, primary_key=True)
    name = models.CharField(max_length=35, verbose_name='Имя')

class Message(models.Model):
    id = models.IntegerField(editable=False, primary_key=True)
    visibility = models.BooleanField(verbose_name='Видимость', default=True)
    chat = models.ForeignKey(Chat, verbose_name='Чат', on_delete = models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete = models.CASCADE, null=True)