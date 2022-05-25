import json



def import_json_chat(file_name):
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)
        print(data['name'])
    return data['name']

