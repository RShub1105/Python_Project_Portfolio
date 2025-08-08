import json
with open ("person.json") as f:
    data=json.load(f)
    print(data)
    print(data['name'])
    