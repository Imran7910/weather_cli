import requests
import json
import sys
BASE_URL="https://api.openweathermap.org/data/2.5/weather"
API_KEY="19e9712d60f01cc61eb6571c9ba428fb"
CITY="london"

request_url = f"{BASE_URL}?q={CITY}&appid={API_KEY}"
try:
    response=requests.get(request_url)
    response.raise_for_status()
    data=response.json()
    city_name=data['name']
    temperature=data['main']['temp']
    humidity=data['main']['humidity']
    weather_description = data['weather'][0]['description']
    print()
    print(f"Weather in {city_name}:")
    print("-" * 20)
    print(f"Temperature: {temperature}K")
    print(f"Humidity: {humidity}%")
    print(f"Conditions: {weather_description.capitalize()}")
    print()
except requests.exceptions.HTTPError as http_err:
    print(f"An HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as e:
    print(f"Network error: Could not connect to the weather service.")
    print(f"Details: {e}")
    sys.exit(1)