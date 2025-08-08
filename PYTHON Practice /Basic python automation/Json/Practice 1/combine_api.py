js
" dasaimport requests
import json

name = "prashant"
url = f"https://api.agify.io?name={name}"
response =requests.get(url)
data = response.json()

with open("agify_result.json","w") as f:
    json.dump(data,f)

print("Api data saved to agify_result.json")
 
