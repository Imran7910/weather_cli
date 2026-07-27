import requests
import json
import sys
BASE_URL="https://api.openweathermap.org/data/2.5/weather"
API_KEY="19e9712d60f01cc61eb6571c9ba428fb"
CITY="london"
def get_weather_data(city, api_key):
    request_url = f"{BASE_URL}?q={CITY}&appid={API_KEY}"
    try:
        response=requests.get(request_url)
        response.raise_for_status()
        data=response.json()
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
        }
        return weather_info
    except requests.exceptions.HTTPError as http_err:
        if http_err.response.status_code == 401:
            print("Error: Invalid API Key. Please check your API_KEY variable.")
        elif http_err.response.status_code == 404:
            print("Error: City not found. Please check the spelling of the city name.")
        else:
            print(f"An HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Network error: Could not connect to the weather service.")
        print(f"Details: {e}")
        return None
API_KEY = "your_actual_api_key_here"  # IMPORTANT: Replace with your key!
CITY = "London"
weather_data = get_weather_data(CITY, API_KEY)
if weather_data:
    print() 
    print(f"Weather in {weather_data['city']}:")
    print("-" * 20) 
    print(f"Temperature: {weather_data['temperature']}K")
    print(f"Humidity: {weather_data['humidity']}%")
    print(f"Conditions: {weather_data['description'].capitalize()}")
    print()