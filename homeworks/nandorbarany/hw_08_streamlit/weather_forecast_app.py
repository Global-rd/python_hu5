import os
from datetime import datetime
import requests
import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_weather_db_connect import SqliteDB


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
DB_PATH = os.path.join(os.path.dirname(__file__), "weather.db")


@st.cache_data(ttl=86400, show_spinner="Waiting for coordinates...")
def get_city_coordinates(city_name):
    parameters = {
        "name": city_name,
        "count": 1
    }
    response = requests.get(url=GEOCODING_URL, params=parameters)

    if response.status_code == 200:
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            return data["results"][0]
        else:
            return None
    else:
        return None


@st.cache_data(ttl=900, show_spinner="Waiting for weather data...")
def get_weather_data(lat, lon):
    parameters = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "hourly": "temperature_2m",
        "forecast_days": 5,
        "timezone": "auto"
    }
    response = requests.get(url=FORECAST_URL, params=parameters)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def show_hourly_data(weather_data):
    if "hourly" in weather_data:
        df = pd.DataFrame(weather_data["hourly"])
        df["timestamp"] = pd.to_datetime(df["time"])
        df.set_index("timestamp", inplace=True)
        df = df.rename(columns={"temperature_2m": "Temperature (°C)"})
        df = df.drop(columns=["time"])
        df = df.sort_index()
        df["Temperature (°C)"] = df["Temperature (°C)"].astype(float)
        return df
    else:
        return None


def log_search_to_db(city, temperature, humidity, wind_speed):
    record = {
        "city": city,
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "search_time": str(datetime.now())
    }
    with SqliteDB(DB_PATH) as db:
        db.create_log_table()
        db.write_single_record("search_log", record)


def main():
    st.title("Weather map & Visualization")

    city_input = st.text_input("Enter city name", "Budapest")

    if city_input:
        location = get_city_coordinates(city_input)

        if location is None:
            st.warning(f"Could not find weather data for '{city_input}'. Please enter an existing city name.")
            return

        city_name = location.get("name", city_input)
        country = location.get("country", "")
        lat = location["latitude"]
        lon = location["longitude"]

        weather_data = get_weather_data(lat, lon)

        if weather_data is None or "current" not in weather_data:
            st.warning("Failed to get weather data from Open-Meteo API.")
            return

        current = weather_data["current"]
        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        wind_speed = current["wind_speed_10m"]

        if st.session_state.get("last_logged_city") != city_name:
            log_search_to_db(city_name, temperature, humidity, wind_speed)
            st.session_state.last_logged_city = city_name

        st.subheader(f"Current weather in {city_name}, {country}")

        kpi_temp, kpi_humidity, kpi_wind = st.columns(3)

        with kpi_temp:
            st.metric(
                label="Temperature (°C)",
                value=f"{temperature}°C"
            )

        with kpi_humidity:
            st.metric(
                label="Humidity (%)",
                value=f"{humidity}%"
            )

        with kpi_wind:
            st.metric(
                label="Wind Speed (km/h)",
                value=f"{wind_speed} km/h"
            )

        st.subheader("Weather Map")
        map_df = pd.DataFrame([{"lat": lat, "lon": lon}])
        st.map(map_df)

        hourly_df = show_hourly_data(weather_data)

        if hourly_df is not None:
            st.subheader("Hourly Temperature Forecast (Next 5 Days)")

            fig_forecast = px.line(
                hourly_df,
                x=hourly_df.index,
                y="Temperature (°C)"
            )
            fig_forecast.update_layout(
                xaxis_title="",
                yaxis_title=""
            )
            st.plotly_chart(fig_forecast)

if __name__ == "__main__":
    main()
