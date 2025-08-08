import requests
import json
Leaders = {
    'Name':'Ratan tata',
    'age': 80,
    'Skills': ['Problem solver','Enterprenure','soft leader']
}
Leaders_json = json.dumps(Leaders)
print(Leaders_json)

# save the dictionary in json file.
with open("Leader.json","w") as f:
    json.dump(Leaders,f)
print("Save to Leader.json file!")

# loading the file and printing the data.
with open("Leader.json") as f:
    data = json.load(f)
    print(data)
    print(data['Name'])

