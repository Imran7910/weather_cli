# 🌤️ Weather CLI

> A fast, minimalistic command-line interface for fetching real-time weather data powered by OpenWeatherMap API.

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)

## 📌 Overview

WeatherCLI is a lightweight Python command-line tool that provides instant, accurate weather forecasts without leaving your terminal workflow. It focuses on speed, simplicity, robust error handling, and clean terminal output.

## ✨ Features

- **Real-Time Weather Data:** Fetches current temperature, feels-like temperature, humidity, and weather conditions.
- **Flexible Location Queries:** Search by city name, including multi-word city names (e.g., "New York", "San Francisco", "London").
- **Multiple Unit Choices:** Support for `--units metric` (°C), `--units imperial` (°F), or `--units standard` (Kelvin).
- **Robust Error Handling:** Informative feedback for invalid city names, missing/invalid API keys, network timeouts, and server errors.

## 🛠️ Tech Stack

- **Language:** Python 3
- **API:** [OpenWeatherMap Current Weather API](https://openweathermap.org/api)
- **Libraries:** `requests`, `python-dotenv`, `argparse`

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Imran7910/weather_cli.git
   cd weather_cli
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key:**
   Create a `.env` file in the root directory and add your OpenWeatherMap API key:
   ```env
   OPENWEATHER_API_KEY=your_api_key_here
   ```

## 💻 Usage

Fetch current weather for a city (defaults to metric / Celsius):
```bash
python weather.py "London"
```

Fetch weather using imperial units (Fahrenheit):
```bash
python weather.py "New York" --units imperial
```

Example Output:
```text
Weather in London, GB:
------------------------------
Temperature: 18.5°C
Feels Like:  18.2°C
Humidity:    68%
Conditions:  Overcast clouds
```

View all command options:
```bash
python weather.py --help
```
