import requests

name = input("Enter the Name = ")
url_age = f"http://api.agify.io?name={name}"
response = requests.get(url_age)
data = response.json()

print(f"Name: {data['name']}")
print(f"Predicted Age: {data['age']}")
print(f"Count: {data['count']}")

age = data['age']

if age >= 18:
    url_joke = "https://v2.jokeapi.dev/joke/Any?type=single"
    response = requests.get(url_joke)
    joke_data = response.json()

    print("Here's a random joke for you:")
    print(joke_data['joke'])
else:
    print("Not valid for joke (age < 18).")
    print("But here’s an adult joke link you could check when you're older:")
    print("https://v2.jokeapi.dev/joke/Any?type=single&blacklistFlags=nsfw")
