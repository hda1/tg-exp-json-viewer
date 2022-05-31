from django.contrib import admin

from .models import *

class ChatAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'name', )

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_id')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_id', 'chat', 'text', 'visibility', 'contact')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('path', 'width', 'height')

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)

admin.site.register(Chat, ChatAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Tag, TagAdmin)