import streamlit as st
import requests
import pandas as pd
import sqlite3
from datetime import datetime
from pathlib import Path

db_path = Path(__file__).with_name("weather_searches.db")
conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS searches (
        city TEXT,
        temperature REAL,
        humidity REAL,
        wind_speed REAL,
        search_time TEXT
    )
""")

conn.commit()

st.title("Weather Dashboard")

city = st.text_input("Enter city name")
search_button = st.button("Search")

if search_button and city:
    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

    geocoding_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    try:
        response = requests.get(
            geocoding_url,
            params=geocoding_params,
            timeout=10
        )
    except requests.RequestException:
        st.warning("Geocoding API request failed.")
        st.stop()

    if response.status_code == 200:
        data = response.json()

        if data.get("results"):
            location = data["results"][0]

            city_name = location["name"]
            country = location["country"]
            latitude = location["latitude"]
            longitude = location["longitude"]
            forecast_url = "https://api.open-meteo.com/v1/forecast"

            forecast_params = {
                "latitude": latitude,
                "longitude": longitude,
                "current": [
                    "temperature_2m",
                    "relative_humidity_2m",
                    "wind_speed_10m"
                ],
                "daily": [
                    "temperature_2m_max",
                    "temperature_2m_min"
                ],
                "timezone": "auto"
            }

            try:
                weather_response = requests.get(
                    forecast_url,
                    params=forecast_params,
                    timeout=10
                )
            except requests.RequestException:
                st.warning("Weather API request failed.")
                st.stop()

            if weather_response.status_code == 200:
                weather_data = weather_response.json()
                current = weather_data["current"]

                temperature = current["temperature_2m"]
                humidity = current["relative_humidity_2m"]
                wind_speed = current["wind_speed_10m"]
                search_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                cursor.execute(
                    """
                    INSERT INTO searches (
                        city,
                        temperature,
                        humidity,
                        wind_speed,
                        search_time
                    )
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        city_name,
                        temperature,
                        humidity,
                        wind_speed,
                        search_time
                    )
                )

                conn.commit()

                st.subheader(f"Current Weather in {city_name}, {country}")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric("Temperature", f"{temperature} °C")

                with col2:
                    st.metric("Humidity", f"{humidity} %")

                with col3:
                    st.metric("Wind speed", f"{wind_speed} km/h")
                daily = weather_data["daily"]

                forecast_df = pd.DataFrame({
                    "Date": pd.to_datetime(daily["time"]),
                    "Max temperature": daily["temperature_2m_max"],
                    "Min temperature": daily["temperature_2m_min"]
                })

                forecast_df = forecast_df.set_index("Date")

                st.subheader("Temperature Forecast")
                st.line_chart(forecast_df)
            else:
                st.warning("Weather API request failed.")

            st.write(f"City: {city_name}")
            st.write(f"Country: {country}")
            st.write(f"Latitude: {latitude}")
            st.write(f"Longitude: {longitude}")
        else:
            st.warning("City not found.")
    else:
        st.warning("Geocoding API request failed.")