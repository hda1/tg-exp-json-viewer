from django.contrib import admin

from .models import *

class ChatAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'name', )

class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_id', 'chat', 'text', 'visibility', 'contact')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_id')

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)

admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Tag, TagAdmin)