import requests
import json

API_KEY = "4b5f5b488022d138c3437cab19a22611"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    print("Weather is : ",weather)
    #print(json.dumps(weather, indent=4, sort_keys=True))
    print("Temperature is : ",temperature, "Celsius")
else:
    print("An error occured......")

