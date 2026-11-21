import streamlit as st
import pandas as pd
import requests

# kell egy konstans a default város nevének tárolására, ha a felhasználó nem ad meg várost
DEFAULT_CITY = "Budapest"

# csinálunk egy függvényt, ami a város nevéből lekéri a földrajzi koordinátákat (latitude és longitude)
def get_location(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search"
    params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }
    response = requests.get(url, params=params)
    location_data = response.json()
    if "results" in location_data and location_data["results"]:
        location = location_data["results"][0]
        latitude = location["latitude"]
        longitude = location["longitude"]
        return latitude, longitude
    else:
        raise ValueError(f"No location data found for city: {city}")

# csinálunk egy másik függvényt, ami a földrajzi koordinátákból lekéri az aktuális időjárási adatokat
def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "hourly": "temperature_2m",
        "forecast_days": 5
    }
    response = requests.get(url, params=params)
    weather_data = response.json()
    return weather_data

# Streamlit alkalmazás felépítése
st.title("Weather Application")
st.caption("Python for Begginners - Homework 8")

# Sidebar a város kereséséhez
with st.sidebar:
    st.header("Location Search")
    city = st.text_input("Enter a city name:", value = DEFAULT_CITY)
    search = st.button("Search")
try:
    latitude, longitude = get_location(city)
    st.success(f"Location found: {city} (Lat: {latitude}, Lon: {longitude})")
except ValueError as error:
    st.error(str(error))
    latitude, longitude = None, None
except requests.exceptions.RequestException as e:
    st.error(f"Couldn't reach the weather service: {e}")
    latitude, longitude = None, None

st.sidebar.write(f"Latitude: {latitude}")
st.sidebar.write(f"Longitude: {longitude}")

# Megjelenítjük a térképet a kiválasztott város koordinátáival (nem hiszem el, hogy ez ennyire egyszerű :))
st.sidebar.map(
    pd.DataFrame({"lat": [latitude], "lon": [longitude]}),
    zoom=9,
    height=200,
)

# Ha a koordináták érvényesek, lekérjük az időjárási adatokat és megjelenítjük azokat
weather = get_weather(latitude, longitude)

current = weather["current"]
st.title(f"Current Weather in {city}")

# 3 egyenlő szélességű oszlopot hozunk létre az aktuális hőmérséklet, páratartalom és szélsebesség megjelenítéséhez
col1, col2, col3 = st.columns(3)
col1.metric("Temperature (°C)", current["temperature_2m"])
col2.metric("Humidity (%)", current["relative_humidity_2m"])
col3.metric("Wind Speed (m/s)", current["wind_speed_10m"])

st.subheader("5-day forecast")

hourly = pd.DataFrame(weather["hourly"])
hourly["time"] = pd.to_datetime(hourly["time"])

# Ez meg még egyszerűbb :) 
st.line_chart(hourly, x="time", y="temperature_2m", y_label="°C")