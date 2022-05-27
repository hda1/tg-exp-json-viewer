from django.db import models

class User(models.Model):
    user = models.CharField(max_length=35, verbose_name='Пользователь')
    user_id = models.CharField(max_length=35, verbose_name='ID')

    class Meta:
        ordering = ['user']
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

class Chat(models.Model):
    chat_id = models.IntegerField(verbose_name='ID', null=True)
    name = models.CharField(max_length=35, verbose_name='Имя')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Tag(models.Model):
    tag = models.CharField(max_length=35, verbose_name='Тег')

    class Meta:
        ordering = ['tag']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Message(models.Model):
    message_id = models.IntegerField(verbose_name='ID', null=True)
    message = models.CharField(max_length=350, verbose_name='Сообщение', default='')
    visibility = models.BooleanField(verbose_name='Видимость', default=True)
    chat = models.ForeignKey(Chat, verbose_name='Чат', on_delete = models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete = models.CASCADE, null=True)
    tag = models.ForeignKey(Tag, verbose_name='Тег', on_delete = models.CASCADE, null=True)

    class Meta:
        ordering = ['message_id']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
