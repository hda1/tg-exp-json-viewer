from django.contrib import admin

from viewer.models import (Chat, Message, User)

class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat')

class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_id')

admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(User, UserAdmin)
