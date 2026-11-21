


import datetime

import pandas as pd
import plotly.express as px
import requests
import streamlit as st


# ==========================================================
# 1. DASHBOARD BEÁLLÍTÁSOK
# ==========================================================

st.set_page_config(
    page_title="Weather Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("Weather Dashboard")

st.markdown(
    """
    <style>
        .stApp {
            background-color: #b1d1c4;
        }
    </style>
    """,
    unsafe_allow_html=True
)

location = st.text_input("Name of the city:")


# ==========================================================
# 2. URL-EK
# ==========================================================

GEOCODING_BASE_URL = (
    "https://geocoding-api.open-meteo.com/v1/search"
)

OPEN_WEATHER_BASE_URL = (
    "https://api.open-meteo.com/v1/forecast"
)


# ==========================================================
# 3. HELYMEGHATÁROZÁS
# ==========================================================

def get_location_coordinates(location):

    params = {
        "name": location,
        "count": 1,
        "language": "hu",
        "format": "json"
    }

    response = requests.get(
        GEOCODING_BASE_URL,
        params=params
    )

    if response.status_code == 200:

        data = response.json()

        if data.get("results"):

            location_data = data["results"][0]

            latitude = location_data["latitude"]
            longitude = location_data["longitude"]
            country = location_data["country"]

            return latitude, longitude, country

        else:
            st.error(f"No location found for {location}")

    else:
        st.error(
            f"Failed to get location coordinates: "
            f"{response.status_code} - {response.text}"
        )

    return None, None, None


# ==========================================================
# 4. IDŐJÁRÁSI ADATOK LEKÉRÉSE
# ==========================================================

def fetch_weather_data(latitude, longitude):

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "wind_speed_10m"
        ),
        "temperature_unit": "celsius",
        "wind_speed_unit": "kmh",
        "forecast_days": 5,
        "timezone": "auto"
    }

    response = requests.get(
        OPEN_WEATHER_BASE_URL,
        params=weather_params
    )

    if response.status_code == 200:
        return response.json()

    st.error(
        f"Failed to fetch data: "
        f"{response.status_code} - {response.text}"
    )

    return None


# ==========================================================
# 5. TÉRKÉP MEGJELENÍTÉSE
# ==========================================================

def show_map(latitude, longitude):

    st.subheader("📍 City location")

    map_data = pd.DataFrame({
        "latitude": [latitude],
        "longitude": [longitude]
    })

    st.map(
        map_data,
        width="stretch",
        height=300
    )


# ==========================================================
# 6. JELENLEGI IDŐJÁRÁS - KPI-OK
# ==========================================================

def show_current_weather(data, location, country):

    current_data = data["current"]

    current_temperature = current_data["temperature_2m"]
    current_humidity = current_data["relative_humidity_2m"]
    current_wind_speed = current_data["wind_speed_10m"]

    st.subheader(
        f"🌤️ Current weather in {location}, {country}"
    )

    col1, col2, col3 = st.columns(3, gap="large")

    col1.metric(
        "🌡️ Temperature",
        f"{current_temperature:.1f} °C"
    )

    col2.metric(
        "💧 Humidity",
        f"{current_humidity:.1f} %"
    )

    col3.metric(
        "💨 Wind speed",
        f"{current_wind_speed:.1f} km/h"
    )


# ==========================================================
# 7. VONALDIAGRAM - ÓRÁNKÉNTI ELŐREJELZÉS
# ==========================================================

def show_temperature_forecast(data, location):

    hourly_data = data["hourly"]

    df_hourly_data = pd.DataFrame({
        "Time": hourly_data["time"],
        "Temperature": hourly_data["temperature_2m"]
    })

    st.subheader(
        f"Hourly Temperature Forecast (Next 5 days), {location}"
    )

    fig = px.line(
        df_hourly_data,
        x="Time",
        y="Temperature",
        height=300,
        color_discrete_sequence=["#dfb228"]
    )

    st.plotly_chart(fig)


# ==========================================================
# 8. FŐPROGRAM
# ==========================================================

def main():

    if not location:
        st.info("Please enter the city:")
        return

    latitude, longitude, country = get_location_coordinates(
        location
    )

    if latitude is None or longitude is None:
        return

    data = fetch_weather_data(latitude, longitude)

    if data is None:
        return

    # Aktuális időjárás
    show_current_weather(data, location, country)

    # Térkép és hőmérsékleti grafikon
    col1, col2 = st.columns(2)

    with col1:
        show_map(latitude, longitude)

    with col2:
        show_temperature_forecast(data, location)


# ==========================================================
# 9. PROGRAM INDÍTÁSA
# ==========================================================

if __name__ == "__main__":
    main()
