import requests
from pprint import pprint

API_Key = "d6426a19c9c46bc11efb1fb67440a41d"

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
