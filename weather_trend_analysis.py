
import pandas as pd
import matplotlib.pyplot as plt
import requests
from datetime import datetime


API_KEY = "xxxxxxxxxxx"  # <-- Replace with your actual API key
CITIES = ["Mumbai", "Pune", "Bangalore", "Delhi"]
URL = "http://api.openweathermap.org/data/2.5/weather"

weather_data = {}

for city in CITIES:
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(URL, params=params)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather_data[city] = temp
    else:
        print(f"Failed to fetch data for {city}")

cities = list(weather_data.keys())
temperatures = list(weather_data.values())

plt.figure(figsize=(10, 6))
plt.bar(cities, temperatures, color='skyblue')
plt.title(f"Current Temperature by City ({datetime.now().strftime('%Y-%m-%d %H:%M')})")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.grid(axis='y')
plt.show()
