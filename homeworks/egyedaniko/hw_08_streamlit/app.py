"""
Weather Dashboard
"""

import requests
import streamlit as st
import pandas as pd


# Oldal beállítása
st.set_page_config(
    page_title="Weather Dashboard",
    page_icon="🌤️",
    layout="wide"
)

st.title("🌤️ Weather Dashboard")


# A városadatokat egy napig tároljuk a gyorsítótárban.
@st.cache_data(ttl=86400)
def get_location(city_name):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city_name,
        "count": 1
    }

    response = requests.get(
        url,
        params=params,
        timeout=30
    )
    response.raise_for_status()

    data = response.json()
    results = data.get("results", [])

    # Nem található a megadott város.
    if not results:
        return None

    return results[0]


# Az időjárásadatok gyorsítótára tíz percig érvényes.
@st.cache_data(ttl=600)
def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "wind_speed_10m"
        ],
        "hourly": ["temperature_2m"],
        "forecast_days": 5,
        "timezone": "auto"
    }

    response = requests.get(
        url,
        params=params,
        timeout=30
    )
    response.raise_for_status()

    return response.json()


# Város bekérése és a szélső szóközök eltávolítása
city_name = st.text_input(
    "Enter city name",
    value="Budapest"
).strip()


if not city_name:
    st.info("Please enter a city name.")

else:
    try:
        location = get_location(city_name)

        if not location:
            st.warning("City not found.")
            st.stop()

        city = location["name"]
        country = location.get("country", "Unknown country")

        latitude = location["latitude"]
        longitude = location["longitude"]

        weather_data = get_weather(latitude, longitude)
        current = weather_data["current"]

        # Aktuális időjárás megjelenítése
        st.header(f"Current Weather in {city}, {country}")

        st.caption(
            f"Local timezone: {weather_data['timezone']} | "
            f"Weather data time: {current['time']}"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Temperature (°C)",
                current["temperature_2m"]
            )

        with col2:
            st.metric(
                "Humidity (%)",
                current["relative_humidity_2m"]
            )

        with col3:
            st.metric(
                "Wind Speed (km/h)",
                current["wind_speed_10m"]
            )

        # Óránkénti adatok DataFrame-be rendezése
        hourly_df = pd.DataFrame(
            {
                "time": weather_data["hourly"]["time"],
                "temperature": (
                    weather_data["hourly"]["temperature_2m"]
                )
            }
        )

        hourly_df["time"] = pd.to_datetime(hourly_df["time"])

        # Az öt nap a mai napot is tartalmazza.
        st.subheader(
            "Hourly Temperature – Today and the Next 4 Days"
        )
        st.caption(
            "Temperature in °C. Times are local to the selected city."
        )

        st.line_chart(
            hourly_df,
            x="time",
            y="temperature"
        )

        # Az előrejelzés táblázatos megjelenítése
        st.subheader("Forecast Data")

        st.dataframe(
            hourly_df,
            hide_index=True
        )

        st.caption("Weather data: Open-Meteo")

    # Hálózati hibák és hibás HTTP-válaszok kezelése
    except requests.exceptions.RequestException as error:
        st.error(f"API request failed: {error}")

    # Hibás vagy hiányos válaszadatok kezelése
    except (KeyError, ValueError, TypeError) as error:
        st.error(f"Unexpected API data: {error}")