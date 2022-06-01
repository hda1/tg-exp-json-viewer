from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=35, verbose_name='Пользователь')
    contact_id = models.CharField(max_length=35, verbose_name='ID')

    class Meta:
        ordering = ['name']
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.name

class Chat(models.Model):
    chat_id = models.IntegerField(verbose_name='ID', null=True)
    name = models.CharField(max_length=35, verbose_name='Имя')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class File(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    mime = models.CharField(max_length=35, verbose_name='Тип')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

class Tag(models.Model):
    tag = models.CharField(max_length=35, verbose_name='Тег')

    class Meta:
        ordering = ['tag']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Photo(models.Model):
    path = models.CharField(max_length=50, verbose_name='Путь')
    width = models.IntegerField(verbose_name='Ширина')
    height = models.IntegerField(verbose_name='Высота')

    class Meta:
        ordering = ['path']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

class Message(models.Model):
    message_id = models.IntegerField(verbose_name='ID', null=True)
    text = models.CharField(max_length=1000, verbose_name='Сообщение', default='')
    visibility = models.BooleanField(verbose_name='Видимость', default=True)
    chat = models.ForeignKey(Chat, verbose_name='Чат', on_delete = models.CASCADE)
    contact = models.ForeignKey(Contact, verbose_name='Пользователь', on_delete = models.CASCADE, null=True)
    tag = models.ForeignKey(Tag, verbose_name='Тег', on_delete = models.CASCADE, null=True, blank=True)
    photo = models.ForeignKey(Photo, verbose_name='Фотография', on_delete = models.CASCADE, null=True)
    file = models.ForeignKey(File, verbose_name='Файл', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['message_id']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.text
