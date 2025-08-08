import json
person = {
    'name': 'Rahul',
    'age': 26,
    'Skills': ['python', 'Apis', 'Automation']
}

person_json = json.dumps(person)
print(person_json)

with open ("person.json","w") as f:
    json.dump(person,f)
    print("Save to a perosn.json")
    