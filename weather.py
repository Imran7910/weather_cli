import argparse
import os
import sys
from dotenv import load_dotenv
import requests

load_dotenv()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

UNIT_SYMBOLS = {
    "metric": "°C",
    "imperial": "°F",
    "standard": "K"
}


def get_weather_data(city, api_key, units="metric"):
    """Fetch current weather data from OpenWeatherMap API for a given city."""
    if not city or not city.strip():
        print("Error: City name cannot be empty.")
        return None

    params = {
        "q": city.strip(),
        "appid": api_key,
        "units": units
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        unit_symbol = UNIT_SYMBOLS.get(units, "")
        weather_info = {
            "city": data["name"],
            "country": data.get("sys", {}).get("country", ""),
            "temperature": data["main"]["temp"],
            "feels_like": data["main"].get("feels_like"),
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "unit_symbol": unit_symbol
        }
        return weather_info

    except requests.exceptions.HTTPError as http_err:
        status_code = http_err.response.status_code if http_err.response is not None else None
        if status_code == 401:
            print("Error: Invalid API Key. Please check your OPENWEATHER_API_KEY variable in .env.")
        elif status_code == 404:
            print(f"Error: City '{city}' not found. Please check the spelling of the city name.")
        elif status_code == 429:
            print("Error: API rate limit exceeded. Please try again later.")
        elif status_code and status_code >= 500:
            print(f"Error: OpenWeather service unavailable ({status_code}). Please try again later.")
        else:
            print(f"An HTTP error occurred ({status_code}): {http_err}")
        return None
    except requests.exceptions.Timeout:
        print("Error: Request timed out while connecting to the weather service.")
        return None
    except requests.exceptions.RequestException as e:
        print("Error: Network error. Could not connect to the weather service.")
        print(f"Details: {e}")
        return None
    except (KeyError, IndexError, ValueError) as parse_err:
        print("Error: Unexpected data format received from weather service.")
        print(f"Details: {parse_err}")
        return None


def display_weather_data(data):
    """Format and print weather details in a readable format."""
    print()
    location = f"{data['city']}, {data['country']}" if data.get("country") else data["city"]
    print(f"Weather in {location}:")
    print("-" * 30)
    symbol = data.get("unit_symbol", "")
    print(f"Temperature: {data['temperature']}{symbol}")
    if data.get("feels_like") is not None:
        print(f"Feels Like:  {data['feels_like']}{symbol}")
    print(f"Humidity:    {data['humidity']}%")
    print(f"Conditions:  {data['description'].capitalize()}")
    print()


def main():
    parser = argparse.ArgumentParser(description="Get the current weather for a specific city.")
    parser.add_argument("city", help="The name of the city to get the weather for.")
    parser.add_argument(
        "--units",
        choices=["metric", "imperial", "standard"],
        default="metric",
        help="The units for temperature (metric=Celsius, imperial=Fahrenheit, standard=Kelvin). Default: metric",
    )
    args = parser.parse_args()

    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("Error: OPENWEATHER_API_KEY not found.")
        print("Please create a .env file and add your API key: OPENWEATHER_API_KEY=your_api_key")
        sys.exit(1)

    weather_data = get_weather_data(args.city, api_key, args.units)
    if weather_data:
        display_weather_data(weather_data)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
