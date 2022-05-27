import json

from .models import Chat, Message

def import_json_chat(file_name):
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)
        chat_name = data['name']
        chat_id = data['id']
        chat_messages = data['messages']

        chat = Chat(chat_id=chat_id, name=chat_name)
        chat.save()

        for message in chat_messages[:10]:
            msg = Message(message_id=message['id'], message=message['text'], chat=chat)
            msg.save()

    return chat_name + ' ' + str(chat_id)

