import json

def import_json_chat(file_name):
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)
        chat_name = data['name']
        chat_id = data['id']
        chat_messages = data['messages']
        for message in chat_messages:
            pass
    return chat_name + ' ' + str(chat_id)

