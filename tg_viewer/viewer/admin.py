from django.contrib import admin

from viewer.models import *

class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat')

class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_id')

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)

admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Tag, TagAdmin)