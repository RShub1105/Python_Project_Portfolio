import requests
import json
Name = input("Enter the Name =")
url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)
data = response.json()
with open("Joke_result.json","w") as f:
    json.dump(data, f , indent=4) 
print("Api datab saved to joke_result.json") 

print("Here's a joke for you, " + Name + "!")
print(data["setup"])
print(data["punchline"])