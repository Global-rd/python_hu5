import streamlit as st
import requests
import pandas as pd
import sqlite3
import time
from datetime import datetime

st.set_page_config(page_title="Weather App", layout="wide")

# --- EXTRA 2: SQLite Adatbázis inicializálása ---
def init_db():
    conn = sqlite3.connect("weather_logs.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS search_logs (
            city TEXT,
            temperature REAL,
            humidity INTEGER,
            wind_speed REAL,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_search(city, temp, hum, wind):
    conn = sqlite3.connect("weather_logs.db")
    cursor = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO search_logs (city, temperature, humidity, wind_speed, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (city, temp, hum, wind, now))
    conn.commit()
    conn.close()

init_db()

# --- API Függvények Cache-eléssel ---
@st.cache_data(ttl=600)
def get_coordinates(city_name):
    host = ".".join(["geocoding-api", "open-meteo", "com"])
    url = f"https://{host}/v1/search"
    params = {"name": city_name, "count": 1, "language": "en", "format": "json"}
    for _ in range(3):
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if "results" in data and len(data["results"]) > 0:
                res = data["results"][0]
                return res["latitude"], res["longitude"], res["name"], res.get("country", "")
            return None
        time.sleep(2)
    raise Exception("Geocoding API limit elérve")

@st.cache_data(ttl=600)
def get_weather_data(lat, lon):
    host = ".".join(["api", "open-meteo", "com"])
    url = f"https://{host}/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "hourly": "temperature_2m",
        "forecast_days": 5,
        "timezone": "auto"
    }
    for _ in range(3):
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
        time.sleep(2)
    raise Exception("Weather API limit elérve")

# --- Felhasználói felület (UI) ---
st.title("Robot Dreams Python - Weather Map & Data Visualization App")

city_input = st.text_input("Enter city name", value="Diósd")

if city_input:
    try:
        geo_data = get_coordinates(city_input)
        
        if geo_data:
            lat, lon, exact_city, country = geo_data
            weather_data = get_weather_data(lat, lon)
            
            current = weather_data["current"]
            temp = current["temperature_2m"]
            hum = current["relative_humidity_2m"]
            wind = current["wind_speed_10m"]
            
            # Adatok mentése az SQLite adatbázisba
            log_search(exact_city, temp, hum, wind)
            
            # Dinamikus fejléc
            st.header(f"Current Weather in {exact_city}, {country}")
            
            # KPI-ok megjelenítése
            col1, col2, col3 = st.columns(3)
            col1.metric("Temperature (°C)", f"{temp}°C")
            col2.metric("Humidity (%)", f"{hum}%")
            col3.metric("Wind Speed (km/h)", f"{wind} km/h")
            
            # Térkép megjelenítése
            st.subheader("Weather Map")
            map_df = pd.DataFrame({"lat": [lat], "lon": [lon]})
            st.map(map_df, zoom=11)
            
            # --- EXTRA 1: 5 napos óránkénti előrejelzés ---
            st.subheader("Hourly Temperature Forecast (Next 5 Days)")
            hourly = weather_data["hourly"]
            forecast_df = pd.DataFrame({
                "Time": pd.to_datetime(hourly["time"]),
                "Temperature": hourly["temperature_2m"]
            })
            forecast_df["Formatted_Time"] = forecast_df["Time"].dt.strftime("%m.%d %H:%M")
            forecast_df = forecast_df.set_index("Formatted_Time")
            
            st.line_chart(forecast_df["Temperature"])
        else:
            st.warning(f"Nem található ilyen város: '{city_input}'.")
            
    except Exception as e:
        st.warning(f"Hiba történt az adatok lekérése közben: {e}")
