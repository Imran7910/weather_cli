import requests
import os
from dotenv import load_dotenv
import argparse
import json
import sys
load_dotenv()
BASE_URL="https://api.openweathermap.org/data/2.5/weather"
def get_weather_data(CITY, API_KEY,units="metrics"):
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
def display_weather_data(data):
    print() 
    print(f"Weather in {data['city']}:")
    print("-" * 20) 
    print(f"Temperature: {data['temperature']}K")
    print(f"Humidity: {data['humidity']}%")
    print(f"Conditions: {data['description'].capitalize()}")
    print()
def main():
    parser = argparse.ArgumentParser(description="Get the current weather for a specific city.")
    parser.add_argument("city", help="The name of the city to get the weather for.")
    parser.add_argument(
        "--units",
        choices=["metric", "imperial"],
        default="metric",
        help="The units for temperature (metric=Celsius, imperial=Fahrenheit). Default: metric",
    )
    args = parser.parse_args()
    API_KEY=os.getenv("OPENWEATHER_API_KEY")
    if not API_KEY:
        print("Error: OPENWEATHER_API_KEY not found.")
        print("Please create a .env file and add your API key to it.")
        sys.exit(1)
    weather_data = get_weather_data(args.city, API_KEY, args.units)
    if weather_data:
        display_weather_data(weather_data)
if __name__ == "__main__":
    main()
