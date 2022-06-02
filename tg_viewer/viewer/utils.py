import json

from .models import Chat, Message, Contact, Photo

def import_json_chat(file_name):
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)
        chat_name = data['name']
        chat_id = data['id']
        chat_messages = data['messages']

        chat, _ = Chat.objects.get_or_create(chat_id=chat_id, name=chat_name)

        for message in chat_messages[:70]:
            if message['type'] == 'service':
                #if message['action'] == 'join_group_by_link':
                #    user, created = User.object.get_or_create(user=message['actor'], user_id=message['actor_id'])
                continue
            if message['type'] == 'message':
                photo_path = message.get('photo', '')
                defaults ={}
                if photo_path:
                    width = message.get('width', 0)
                    height = message.get('height', 0)
                    print(photo_path)
                    photo, _ = Photo.objects.get_or_create(path=photo_path, defaults={'width': width, 'height': height})
                    defaults['photo'] = photo
                #user_id = message['from_id']
                #defaults['photo'] = photo
                #user_name = message['from']
                #defaults['photo'] = photo
                contact, _ = Contact.objects.get_or_create(contact_id=message['from_id'], name=message['from'])
                defaults['contact'] = contact
                defaults['text'] = message['text']
                defaults['chat'] = chat
                defaults['visibility'] = True
                msg, _ = Message.objects.get_or_create(message_id=message['id'], defaults=defaults)


    return chat_name + ' ' + str(chat_id)

