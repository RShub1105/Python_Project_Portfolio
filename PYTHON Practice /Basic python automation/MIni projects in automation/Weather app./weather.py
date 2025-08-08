import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("API_KEY")
print("API_KEY:",API_KEY)
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data. Status code:", response.status_code)
        return None

def save_weather(data):
    with open("weather.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Weather data saved to weather.json")

def main():
    city = input("Enter the city name: ")
    data = get_weather(city)
    if data:
        print(f"Weather in {city}: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']}℃")
        save_weather(data)

if __name__ == "__main__":
    main()
