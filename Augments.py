import json

def getAugDict():
    with open('augments.json' , 'r+') as file:
        data = file.read()
        augments = json.loads(data)

    id_to_name = {augment['id']: augment['name'] for augment in augments['augments']}
    return id_to_name
