
import requests
import pandas as pd
import streamlit as st


# Oldal beallitasa
st.set_page_config(
    page_title="Weather Dashboard",
    page_icon="🌤️",
    layout="wide"
)

st.title("🌤️ Weather Map & Data Visualization")
st.write("Interaktiv idojaras dashboard az Open-Meteo API adataival.")


# Varos koordinatainak lekerdezese
def get_coordinates(city_name):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    response = requests.get(
        url,
        params={
            "name": city_name,
            "count": 1,
            "language": "hu",
            "format": "json"
        },
        timeout=10
    )
    response.raise_for_status()

    results = response.json().get("results", [])

    if not results:
        return None

    return results[0]


# Idojarasi adatok lekerdezese
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
        "hourly": "temperature_2m",
        "forecast_days": 5,
        "timezone": "auto"
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )
    response.raise_for_status()

    return response.json()


# Varos megadasa
city = st.text_input(
    "Add meg a varos nevet:",
    value="Budapest"
)


if city.strip():
    try:
        location = get_coordinates(city.strip())

        if location is None:
            st.warning("A megadott varos nem talalhato.")
            st.stop()

        city_name = location["name"]
        country = location.get("country", "")
        latitude = location["latitude"]
        longitude = location["longitude"]

        weather = get_weather(latitude, longitude)
        current = weather["current"]

        st.subheader(
            f"Current Weather in {city_name}, {country}"
        )

        # KPI-ok
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Temperature (°C)",
                f"{current['temperature_2m']:.1f} °C"
            )

        with col2:
            st.metric(
                "Humidity (%)",
                f"{current['relative_humidity_2m']} %"
            )

        with col3:
            st.metric(
                "Wind Speed (km/h)",
                f"{current['wind_speed_10m']:.1f} km/h"
            )

        # Terkep
        st.subheader(f"Weather Map – {city_name}")

        map_data = pd.DataFrame({
            "lat": [latitude],
            "lon": [longitude]
        })

        st.map(map_data, zoom=10)

        # Orai homersekleti elorejelzes
        st.subheader(
            f"Hourly Temperature Forecast – {city_name}"
        )

        hourly = weather["hourly"]

        forecast_data = pd.DataFrame({
            "Time": pd.to_datetime(hourly["time"]),
            "Temperature (°C)": hourly["temperature_2m"]
        })

        forecast_data = forecast_data.set_index("Time")

        st.line_chart(
            forecast_data,
            y="Temperature (°C)"
        )

    except requests.exceptions.RequestException:
        st.warning(
            "Nem sikerult lekerdezni az idojarasi adatokat. "
            "Probald ujra kesobb."
        )

    except (KeyError, ValueError, TypeError):
        st.warning(
            "Hiba tortent az idojarasi adatok feldolgozasakor."
        )

else:
    st.info("Adj meg egy varosnevet az adatok megjelenitesehez.")
