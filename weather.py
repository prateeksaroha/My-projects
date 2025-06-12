
import pandas as pd
import matplotlib.pyplot as plt


api_key = "2595f3bb86d69a384349a7487c42e421"
city = "Delhi"
lat = 28.6139
lon = 77.2090

url = "https://api.openweathermap.org/data/2.5/onecall/timemachine"
params = {
    "lat": lat,
    "lon": lon,
    "dt": 1680000000,
    "appid": api_key
}

response = requests.get(url, params=params)
data = response.json()

temperatures = [hour["temp"] - 273.15 for hour in data["hourly"]]  
timestamps = [hour["dt"] for hour in data["hourly"]]
dates = pd.to_datetime(timestamps, unit='s')

df = pd.DataFrame({
    "Date": dates,
    "Temperature (°C)": temperatures
})

plt.figure(figsize=(10, 6))
plt.plot(df["Date"], df["Temperature (°C)"], marker='o', linestyle='-', color='b')
plt.title(f"Temperature Trend in {city} on {dates[0].strftime('%Y-%m-%d')}")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
