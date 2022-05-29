import json

from .models import Chat, Message, Contact

def import_json_chat(file_name):
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)
        chat_name = data['name']
        chat_id = data['id']
        chat_messages = data['messages']

        chat, _ = Chat.objects.get_or_create(chat_id=chat_id, name=chat_name)

        for message in chat_messages[:60]:
            if message['type'] == 'service':
                #if message['action'] == 'join_group_by_link':
                #    user, created = User.object.get_or_create(user=message['actor'], user_id=message['actor_id'])
                continue
            if message['type'] == 'message':
                user_id = message['from_id']
                user_name = message['from']
                contact, _ = Contact.objects.get_or_create(contact_id=message['from_id'], name=message['from'])
                msg, _ = Message.objects.get_or_create(message_id=message['id'], defaults={'text':message['text'], 'chat':chat, 'contact':contact, 'visibility': True})


    return chat_name + ' ' + str(chat_id)

