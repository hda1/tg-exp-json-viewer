from django.contrib import admin

from viewer.models import (Chat, Message, )

class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat')

admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)

