import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime
from database import init_db, save_search


# ------------------------------------------------
# Oldal beállítás
# ------------------------------------------------

st.set_page_config(
    page_title="Weather Dashboard",
    page_icon="🌤️",
    layout="wide"
)

init_db()

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


# ------------------------------------------------
# Fejléc
# ------------------------------------------------

st.title("🌤️ Weather Dashboard")
st.markdown("Valós idejű időjárási adatok Open-Meteo API segítségével")


# ------------------------------------------------
# Sidebar
# ------------------------------------------------

st.sidebar.header("Keresés")

city = st.sidebar.text_input(
    "Város neve",
    value="Budapest"
)


# ------------------------------------------------
# Lekérdezés
# ------------------------------------------------

if city:

    try:

        # ----------------------------
        # Geocoding API
        # ----------------------------

        geo_response = requests.get(
            GEOCODING_URL,
            params={
                "name": city,
                "count": 1,
                "language": "en",
                "format": "json"
            }
        )

        geo_data = geo_response.json()

        if "results" not in geo_data:
            st.warning("⚠️ A város nem található.")
            st.stop()

        location = geo_data["results"][0]

        city_name = location["name"]
        country_name = location["country"]

        latitude = location["latitude"]
        longitude = location["longitude"]

        # ----------------------------
        # Forecast API
        # ----------------------------

        forecast_response = requests.get(
            FORECAST_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
                "hourly": "temperature_2m",
                "forecast_days": 3
            }
        )

        weather_data = forecast_response.json()

        current = weather_data["current"]

        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        wind_speed = current["wind_speed_10m"]

        # ----------------------------
        # Mentés SQLite-ba
        # ----------------------------

        save_search(
            city_name,
            temperature,
            humidity,
            wind_speed,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        # ----------------------------
        # Fejléc
        # ----------------------------

        st.subheader(f"📍 {city_name}, {country_name}")

        # ----------------------------
        # KPI adatok
        # ----------------------------

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "🌡️ Hőmérséklet",
                f"{temperature} °C"
            )

        with col2:
            st.metric(
                "💧 Páratartalom",
                f"{humidity} %"
            )

        with col3:
            st.metric(
                "🌬️ Szélsebesség",
                f"{wind_speed} km/h"
            )

        st.divider()

        # ----------------------------
        # Tabok
        # ----------------------------

        tab1, tab2, tab3 = st.tabs(
            [
                "📈 Előrejelzés",
                "🗺️ Térkép",
                "📋 API Adatok"
            ]
        )

        # =================================================
        # Előrejelzés
        # =================================================

        with tab1:

            forecast_df = pd.DataFrame({
                "Időpont": weather_data["hourly"]["time"],
                "Hőmérséklet": weather_data["hourly"]["temperature_2m"]
            })

            fig = px.line(
                forecast_df,
                x="Időpont",
                y="Hőmérséklet",
                title=f"Hőmérséklet előrejelzés - {city_name}",
                markers=True
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        # =================================================
        # Térkép
        # =================================================

        with tab2:

            st.subheader(
                f"🗺️ {city_name} elhelyezkedése"
            )

            map_data = pd.DataFrame({
                "lat": [latitude],
                "lon": [longitude]
            })

            st.map(
                map_data,
                zoom=10
            )

            st.info(
                f"""
                Város: {city_name}

                Ország: {country_name}

                Latitude: {latitude}

                Longitude: {longitude}
                """
            )

        # =================================================
        # Nyers API válasz
        # =================================================

        with tab3:
            st.json(weather_data)

    except Exception as e:

        st.warning(
            f"⚠️ Hiba történt: {e}"
        )