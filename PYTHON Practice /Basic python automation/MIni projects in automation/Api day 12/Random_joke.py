import requests
url="https://official-joke-api.appspot.com/random_joke"
response=requests.get(url)
joke=response.json()
print(joke['setup'])
print(joke['punchline'])
