from django.db import models

class Chat(models.Model):
    id = models.IntegerField(editable=False, primary_key=True)
    name = models.CharField(max_length=35, verbose_name="Имя")

class Message(models.Model):
    id = models.IntegerField(editable=False, primary_key=True)

    chat = models.ForeignKey(Chat, verbose_name='Чат', on_delete = models.CASCADE)