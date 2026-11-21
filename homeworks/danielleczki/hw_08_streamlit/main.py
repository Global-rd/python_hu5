import streamlit as st
import pandas as pd
import requests
import sqlite3
from datetime import datetime
from pathlib import Path


GEO_BASE_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_BASE_URL = "https://api.open-meteo.com/v1/forecast"

DB_PATH = Path(__file__).parent / "weather_logs.db"

def init_db():
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS search_logs (
            city_name TEXT,
            temperature REAL,
            humidity REAL,
            wind_speed REAL,
            searched_at TEXT
        )
    """)
    conn.commit()
    conn.close()


def log_search_to_db(city_name, temperature, humidity, wind_speed):
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO search_logs (city_name, temperature, humidity, wind_speed, searched_at)
        VALUES (?, ?, ?, ?, ?)
    """, (city_name, temperature, humidity, wind_speed, current_time))
    conn.commit()
    conn.close()


@st.cache_data(ttl=86400, show_spinner="Searching for city...")
def fetch_city_coordinates(city_name):
    url = f"{GEO_BASE_URL}?name={city_name}&count=1&language=en&format=json"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if "results" in data and len(data["results"]) > 0:
                return data["results"][0]
            else:
                st.warning(f"Nem található ilyen település: '{city_name}'. Kérlek, ellenőrizd a nevet!")
                return None
        else:
            st.warning(f"Hiba történt a helymeghatározó API hívásakor (Státuszkód: {response.status_code}).")
            return None
    except requests.RequestException as e:
        st.warning(f"Hálózati hiba az API elérésekor: {e}")
        return None


@st.cache_data(ttl=3600, show_spinner="Fetching weather data...")
def fetch_weather_data(lat, lon):
    url = (
        f"{WEATHER_BASE_URL}?"
        f"latitude={lat}&longitude={lon}"
        f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
        f"&hourly=temperature_2m"
        f"&forecast_days=5"
        f"&timezone=auto"
    )
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            st.warning(f"Hiba történt az időjárás API hívásakor (Státuszkód: {response.status_code}).")
            return None
    except requests.RequestException as e:
        st.warning(f"Hálózati hiba az időjárás adatok lekérésekor: {e}")
        return None


def process_hourly_data(weather_data):
    if "hourly" in weather_data:
        hourly = weather_data["hourly"]
        df = pd.DataFrame({
            "timestamp": pd.to_datetime(hourly["time"]),
            "Temperature": hourly["temperature_2m"]
        })
        df["Formatted Time"] = df["timestamp"].dt.strftime("%m.%d %H:%M")
        df.set_index("Formatted Time", inplace=True)
        df.drop(columns=["timestamp"], inplace=True)
        return df
    else:
        st.warning("Nem érhető el óránkénti előrejelzési adat.")
        return None


def main():
    
    init_db()

    st.markdown(
    """
    <h1 style="text-align: center;">
        Weather Map & Data Visualization App
    </h1>
    <h3 style="text-align: center;">
        By Dani
    </h3>
    """,
    unsafe_allow_html=True
)

    city = st.text_input("Enter city name", "München")

    if city:
        location = fetch_city_coordinates(city)

        if location:
            lat = location["latitude"]
            lon = location["longitude"]
            city_name = location["name"]
            country = location.get("country", "")

            weather_data = fetch_weather_data(lat, lon)

            if weather_data and "current" in weather_data:
                current = weather_data["current"]
                temp = current["temperature_2m"]
                humidity = current["relative_humidity_2m"]
                wind_speed = current["wind_speed_10m"]

                
                if st.session_state.get("last_logged_city") != city_name:
                    log_search_to_db(city_name, temp, humidity, wind_speed)
                    st.session_state["last_logged_city"] = city_name

              
                header_text = f"Current Weather in {city_name}, {country}" if country else f"Current Weather in {city_name}"
                st.header(header_text)

                
                kpi_temp, kpi_humidity, kpi_wind = st.columns(3)

                with kpi_temp:
                    st.metric(label="Temperature (°C)", value=f"{temp}°C")

                with kpi_humidity:
                    st.metric(label="Humidity (%)", value=f"{humidity}%")

                with kpi_wind:
                    st.metric(label="Wind Speed (km/h)", value=f"{wind_speed} km/h")

                
                st.subheader("Weather Map")
                map_df = pd.DataFrame({"lat": [lat], "lon": [lon]})
                st.map(map_df, zoom=10)

                
                st.subheader("Hourly Temperature Forecast (Next 5 Days)")
                df_hourly = process_hourly_data(weather_data)

                if df_hourly is not None:
                    st.line_chart(df_hourly["Temperature"])


if __name__ == "__main__":
    main()