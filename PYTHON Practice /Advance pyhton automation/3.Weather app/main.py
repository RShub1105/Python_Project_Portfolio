import requests
API_KEY="fee7d994eb5be5cdc01be0a4d71595e9"
print("API key loaded.")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
def get_weather(city):
    params = {
         'q':city,
        'appid': API_KEY,
        'units':'metric'
    }
    try:
        response = requests.get(BASE_URL,params=params)
        data = response.json()
        if response.status_code == 200:
            print(f"Weather in {data['name']}, {data['sys']['country']}")
            print(f"Temperature : {data['main']['temp']}℃")
            print(f"Feels like : {data['main']['feels_like']}℃")
            print(f"weather : {data['weather'][0]['description'].title()}")
        else:
            print("City not found.please try again!")
    except Exception as e :
        print("Error featching weather data", str(e))

while True:
    city = input("\nEnter city name (or write( Exit to quit )): ").strip()
    if city.lower() == 'exit':
        city.upper =='Exit'
        print("Good byee👋🏻")
        break
    get_weather(city)
