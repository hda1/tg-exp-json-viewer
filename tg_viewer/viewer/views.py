from django.http import HttpResponse

from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework.viewsets import ModelViewSet

from .models import Message
from .serializers import MessageSerializer
from .utils import import_json_chat

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.filter(visibility=True)[:5]
        return context

class MainAppView(TemplateView):
    template_name = "main_app.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ImportView(TemplateView):

    def get(self, request, *args, **kwargs):
        file_name = '/home/sam/Загрузки/Telegram Desktop/ChatExport_2022-05-15/result.json'
        chat_name = import_json_chat(file_name)
        return HttpResponse('Chat ' + chat_name)

class MessageView(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
