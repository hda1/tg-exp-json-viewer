from django.http import HttpResponse

from django.shortcuts import render
from django.views.generic.base import TemplateView

from viewer.models import Message
from viewer.utils import import_json_chat

class HomePageView(TemplateView):

    def get(self, request, *args, **kwargs):
        file_name = '/home/sam/Загрузки/Telegram Desktop/ChatExport_2022-05-15/result.json'
        chat_name = import_json_chat(file_name)
        return HttpResponse('Hello, World! ' + chat_name)
    #template_name = "home.html"
"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Message.objects.all()[:5]
        return context
"""

class ImportView(TemplateView):

    def get(self, request, *args, **kwargs):
        file_name = '/home/sam/Загрузки/Telegram Desktop/ChatExport_2022-05-15/result.json'
        chat_name = import_json_chat(file_name)
        return HttpResponse('Chat ' + chat_name)