import requests
name = "Rahul"
url=f"https://api.agify.io?name={name}"
response=requests.get(url)
data=response.json()

print(f"Name:{data['name']}")
print(f"Predict age:{data['age']}")
print(f"Count:{data['count']}")
