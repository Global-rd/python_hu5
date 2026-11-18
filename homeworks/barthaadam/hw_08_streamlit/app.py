# Könyvtárak és alapbeállítások

import sqlite3
from datetime import datetime
from pathlib import Path

import pandas as pd
import requests
import streamlit as st


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
DB_PATH = Path(__file__).resolve().parent / "weather_searches.db"


# Adatok lekérése az API-kból

def get_json(url, params):
    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()
    data = response.json()

    if not isinstance(data, dict):
        raise ValueError(
            "Az időjárás-szolgáltató válasza nem értelmezhető."
        )

    if data.get("error"):
        raise ValueError(
            data.get("reason", "A szolgáltató hibát jelzett.")
        )

    return data


def get_location(city_name):
    params = {
        "name": city_name,
        "count": 1,
        "language": "hu",
        "format": "json",
    }

    data = get_json(GEOCODING_URL, params)
    locations = data.get("results", [])

    if not locations:
        raise ValueError(
            f"Nem található ilyen település: {city_name}."
        )

    return locations[0]


def get_weather(latitude, longitude):
    variables = (
        "temperature_2m,"
        "relative_humidity_2m,"
        "wind_speed_10m"
    )

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": variables,
        "hourly": variables,
        "forecast_hours": 120,
        "temperature_unit": "celsius",
        "wind_speed_unit": "kmh",
        "timezone": "auto",
    }

    data = get_json(FORECAST_URL, params)

    required = [
        "time",
        "temperature_2m",
        "relative_humidity_2m",
        "wind_speed_10m",
    ]

    if any(
        key not in data.get("current", {})
        for key in required
    ):
        raise ValueError(
            "A szolgáltató hiányos aktuális időjárásadatot adott vissza."
        )

    if any(
        key not in data.get("hourly", {})
        for key in required
    ):
        raise ValueError(
            "A szolgáltató hiányos előrejelzést adott vissza."
        )

    return data


# Keresések naplózása SQLite-adatbázisba

def log_search(city_name, current):
    with sqlite3.connect(DB_PATH, timeout=10) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS search_history (
                city_name TEXT NOT NULL,
                temperature REAL,
                humidity REAL,
                wind_speed REAL,
                searched_at TEXT NOT NULL
            )
            """
        )

        connection.execute(
            """
            INSERT INTO search_history
                (
                    city_name,
                    temperature,
                    humidity,
                    wind_speed,
                    searched_at
                )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                city_name,
                current.get("temperature_2m"),
                current.get("relative_humidity_2m"),
                current.get("wind_speed_10m"),
                datetime.now().isoformat(timespec="seconds"),
            ),
        )


# Az alkalmazás felülete és a városnév bekérése

def main():
    st.set_page_config(
        page_title="Városi időjárás",
        page_icon="🌤️",
        layout="wide",
    )

    st.title("🌤️ Városi időjárás")
    st.caption(
        "Aktuális időjárás és öt nap óránkénti előrejelzése egy helyen."
    )

    with st.sidebar:
        st.header("Városkereső")

        with st.form("city_search"):
            city_name = st.text_input(
                "Város neve",
                value="Nyíregyháza",
                help=(
                    "Azonos városneveknél az országot is megadhatod: "
                    "Paris, France."
                ),
            )

            submitted = st.form_submit_button(
                "Időjárás lekérése",
                width="stretch",
            )

        st.caption(
            "Írd be a várost, majd kattints az Időjárás lekérése gombra."
        )

    # A keresés feldolgozása, az adatok tárolása és a hibák kezelése

    if submitted:
        st.session_state.pop("weather_result", None)
        search_name = city_name.strip()
        current = {}

        try:
            if len(search_name) < 2:
                raise ValueError(
                    "Adj meg egy legalább két karakteres városnevet."
                )

            with st.spinner("Időjárási adatok lekérése..."):
                location = get_location(search_name)

                country = location.get(
                    "country",
                    location.get("country_code", ""),
                )

                place = ", ".join(
                    part
                    for part in [location["name"], country]
                    if part
                )

                search_name = place

                weather = get_weather(
                    location["latitude"],
                    location["longitude"],
                )

                hourly_df = pd.DataFrame(weather["hourly"])
                hourly_df["time"] = pd.to_datetime(hourly_df["time"])

                hourly_df = hourly_df.rename(
                    columns={
                        "time": "Időpont",
                        "temperature_2m": "Hőmérséklet (°C)",
                        "relative_humidity_2m": "Páratartalom (%)",
                        "wind_speed_10m": "Szélsebesség (km/h)",
                    }
                )

                current = weather["current"]

                st.session_state["weather_result"] = {
                    "place": place,
                    "location": location,
                    "weather": weather,
                    "hourly_df": hourly_df,
                }

        except requests.RequestException:
            st.warning(
                "Nem sikerült elérni az időjárás-szolgáltatót. "
                "Próbáld újra később."
            )

        except (KeyError, TypeError, ValueError) as error:
            st.warning(f"A keresés nem sikerült. {error}")

        try:
            log_search(search_name, current)

        except sqlite3.Error:
            st.warning("A keresés naplózása most nem sikerült.")

    if "weather_result" not in st.session_state:
        st.info(
            "A kezdéshez keress rá egy városra a bal oldali panelen."
        )
        st.stop()

    # Az aktuális időjárás megjelenítése három KPI-kártyán

    result = st.session_state["weather_result"]

    place = result["place"]
    location = result["location"]
    weather = result["weather"]
    hourly_df = result["hourly_df"]
    current = weather["current"]

    st.subheader(f"Aktuális időjárás: {place}")

    updated_at = pd.Timestamp(current["time"]).strftime(
        "%Y. %m. %d. %H:%M"
    )

    st.caption(
        f"Adat időpontja: {updated_at} · "
        f"Időzóna: {weather.get('timezone', 'GMT')}"
    )

    temperature = current["temperature_2m"]
    humidity = current["relative_humidity_2m"]
    wind_speed = current["wind_speed_10m"]

    column1, column2, column3 = st.columns(3)

    column1.metric(
        "🌡️ Hőmérséklet",
        f"{temperature:.1f} °C"
        if temperature is not None
        else "Nincs adat",
        border=True,
    )

    column2.metric(
        "💧 Páratartalom",
        f"{humidity:.0f} %"
        if humidity is not None
        else "Nincs adat",
        border=True,
    )

    column3.metric(
        "💨 Szélsebesség",
        f"{wind_speed:.1f} km/h"
        if wind_speed is not None
        else "Nincs adat",
        border=True,
    )

    # Az előrejelzési grafikonok megjelenítése

    forecast_tab, map_tab, data_tab = st.tabs(
        ["Előrejelzés", "Térkép", "Adatok"]
    )

    with forecast_tab:
        st.subheader(f"Óránkénti hőmérséklet: {place}")

        st.caption(
            "120 órás előrejelzés a jelenlegi órától; "
            "az időpontok helyi időben szerepelnek."
        )

        st.line_chart(
            hourly_df,
            x="Időpont",
            y="Hőmérséklet (°C)",
            color="#38bdf8",
            height=300,
        )

        left, right = st.columns(2)

        with left:
            st.markdown("**Páratartalom**")

            st.line_chart(
                hourly_df,
                x="Időpont",
                y="Páratartalom (%)",
                color="#2dd4bf",
                height=220,
            )

        with right:
            st.markdown("**Szélsebesség**")

            st.line_chart(
                hourly_df,
                x="Időpont",
                y="Szélsebesség (km/h)",
                color="#fbbf24",
                height=220,
            )

    # A település térképe és az előrejelzés adattáblája

    with map_tab:
        st.subheader(f"A település helye: {place}")

        map_df = pd.DataFrame(
            {
                "latitude": [location["latitude"]],
                "longitude": [location["longitude"]],
            }
        )

        st.map(
            map_df,
            zoom=10,
            height=450,
        )

    with data_tab:
        st.subheader(f"Előrejelzési adatok: {place}")

        st.dataframe(
            hourly_df,
            hide_index=True,
            width="stretch",
        )

    st.caption(
        "Adatforrás: [Open-Meteo](https://open-meteo.com/) · "
        "Helyadatok: GeoNames"
    )


# Az alkalmazás indítása

if __name__ == "__main__":
    main()