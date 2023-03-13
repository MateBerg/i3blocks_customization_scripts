#!/usr/bin/env python3

import requests
import json
import subprocess
import time 

# Your weather API key here
API_KEY = "333cb1cac23c4e1ca88205459231103"

# Your location here
LOCATION = "Cairo"

# Emojis for different weather conditions
emojis = {
    "Sunny": "☀️",
    "Clear": "☀️",
    "Partly cloudy": "⛅",
    "Cloudy": "☁️",
    "Overcast": "☁️",
    "Mist": "🌫️",
    "Fog": "🌁",
    "Light rain": "🌧️",
    "Moderate rain": "🌧️",
    "Heavy rain": "🌧️☔",
    "Patchy rain possible": "🌦️",
    "Patchy snow possible": "🌨️",
    "Patchy sleet possible": "🌨️",
    "Patchy freezing drizzle possible": "🌨️",
    "Light snow": "🌨️",
    "Moderate snow": "🌨️",
    "Heavy snow": "❄️",
    "Ice pellets": "🌨️",
    "Light rain shower": "🌦️",
    "Moderate or heavy rain shower": "🌧️",
    "Torrential rain shower": "🌧️☔",
    "Light sleet": "🌨️",
    "Moderate or heavy sleet": "🌨️",
    "Light snow showers": "🌨️",
    "Moderate or heavy snow showers": "❄️",
    "Light showers of ice pellets": "🌨️",
    "Moderate or heavy showers of ice pellets": "🌨️",
    "Patchy light rain with thunder": "⛈️",
    "Moderate or heavy rain with thunder": "⛈️🌧️",
    "Patchy light snow with thunder": "🌨️⛈️",
    "Moderate or heavy snow with thunder": "🌨️⛈️❄️"
}

# Get weather data
url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={LOCATION}&aqi=no"
response = requests.get(url)

# Parse JSON response
data = json.loads(response.text)

# Extract temperature and weather condition
temp_c = data["current"]["temp_c"]
condition = data["current"]["condition"]["text"]
humidity = data["current"]["humidity"]
emoji = emojis.get(condition, "🤔")

# Bitcoin Info
response2 = requests.get('https://api.coinbase.com/v2/prices/spot?currency=USD')
data = json.loads(response2.text)
price = data['data']['amount']

# USD to EGP info
# Make API request to get USD to EGP exchange rate
response3 = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
data = response3.json()
# Get USD to EGP exchange rate
rate = data['rates']['EGP']



# Print formatted weather information
print(f"{temp_c}°C {emoji} {condition} {humidity}")
command = f"notify-send '🌡️T: {int(temp_c)}°C | {emoji} {condition} | H:💧{humidity}% \n 1 🇺🇸 = {rate} 🇪🇬 | 🪙 {price} 💲 '"
subprocess.call(command,  shell=True)
