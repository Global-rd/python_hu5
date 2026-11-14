
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

# 1. Az alkalmazás alapbeállításai
st.set_page_config(
    page_title="Weather Dashboard",
    page_icon="⛅",
    layout="centered"
)

# 2. API-végpontok
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"



# SQLite adatbázis helye
DB_PATH = Path(__file__).with_name("weather_history.db")


def init_database():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS weather_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT NOT NULL,
                country TEXT,
                temperature REAL,
                humidity REAL,
                wind_speed REAL,
                searched_at TEXT NOT NULL
            )
        """)


def save_weather(city, country, current):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            INSERT INTO weather_history (
                city,
                country,
                temperature,
                humidity,
                wind_speed,
                searched_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            city,
            country,
            current["temperature_2m"],
            current["relative_humidity_2m"],
            current["wind_speed_10m"],
            datetime.now(timezone.utc).isoformat(
                timespec="seconds"
            )
        ))



# Korábbi keresések visszaolvasása
def load_weather_history():
    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query("""
            SELECT
                city,
                country,
                temperature,
                humidity,
                wind_speed,
                searched_at
            FROM weather_history
            ORDER BY id DESC
            LIMIT 20
        """, conn)

    return df



# 3. Városkereső függvény
def find_city(city_name):
    params = {
        "name": city_name,
        "count": 1,
        "language": "hu"
    }

    try:
        response = requests.get(
            GEOCODING_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()
        data = response.json()

    except (requests.exceptions.RequestException, ValueError):
        st.warning("Nem sikerült lekérni a város adatait.")
        return None

    results = data.get("results", [])

    if not results:
        st.warning("Nem található ilyen város.")
        return None

    return results[0]


# 4. Időjárás-lekérő függvény

def fetch_weather(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "hourly": "temperature_2m,relative_humidity_2m",
        "forecast_days": 5,
        "timezone": "auto"
    }

    try:
        response = requests.get(
            FORECAST_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()
        data = response.json()

        return data

    except (requests.exceptions.RequestException, ValueError):
        st.warning("Nem sikerült lekérni az időjárásadatokat.")
        return None

# Adatbázis inicializálása
init_database()

# 5. A kiválasztott város megőrzése
if "city" not in st.session_state:
    st.session_state.city = "Győr"


# 6. Cím és városkereső
st.title("⛅ Weather Dashboard")
st.caption("Interaktív időjárás-alkalmazás")

with st.form("city_form"):
    city_input = st.text_input(
        "Melyik város időjárása érdekel?",
        value=st.session_state.city
    )

    submitted = st.form_submit_button("Keresés")

if submitted:
    if city_input.strip():
        st.session_state.city = city_input.strip()
    else:
        st.warning("Kérlek, adj meg egy városnevet!")
        st.stop()


# 7. Város adatainak lekérése
location = find_city(st.session_state.city)

if location:
    city_name = location["name"]
    country = location.get("country", "Ismeretlen ország")
    latitude = location["latitude"]
    longitude = location["longitude"]

    st.header(f"📍 {city_name}, {country}")

    st.write(f"Szélességi fok: {latitude:.4f}")
    st.write(f"Hosszúsági fok: {longitude:.4f}")


    # A kiválasztott város megjelenítése térképen
    st.subheader("🗺️ Időjárási térkép")

    map_df = pd.DataFrame({
        "lat": [latitude],
        "lon": [longitude]
    })

    st.map(
        map_df,
        zoom=10,
        size=500,
        height=350
    )


    # 8. Időjárásadatok lekérése
    weather = fetch_weather(latitude, longitude)



    if weather:
        current = weather["current"]

        if submitted:
            save_weather(city_name, country, current)
            st.success("Az időjárási adatok mentve az adatbázisba!")

        st.subheader("Aktuális időjárás")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Hőmérséklet",
                f"{current['temperature_2m']} °C"
            )

        with col2:
            st.metric(
                "Páratartalom",
                f"{current['relative_humidity_2m']} %"
            )

        with col3:
            st.metric(
                "Szélsebesség",
                f"{current['wind_speed_10m']} km/h"
            )

        # Óránkénti adatok feldolgozása
        hourly = weather.get("hourly")

        if hourly and hourly.get("time"):
            df = pd.DataFrame(hourly)

            df["time"] = pd.to_datetime(df["time"])

            st.subheader("5 napos előrejelzés")

            tab1, tab2 = st.tabs([
                "🌡️ Hőmérséklet",
                "💧 Páratartalom"
            ])

            with tab1:
                fig_temp = px.line(
                    df,
                    x="time",
                    y="temperature_2m",
                    title="Hőmérséklet alakulása",
                    labels={
                        "time": "Időpont",
                        "temperature_2m": "Hőmérséklet (°C)"
                    },
                    markers=False
                )

                # X-tengely: 4 óránként, éjféltől
                fig_temp.update_xaxes(
                    tickmode="linear",
                    tick0=df["time"].min().normalize(),
                    dtick=4 * 60 * 60 * 1000,
                    tickformat="%m.%d %H:%M",
                    tickangle=-90,
                    side="bottom",
                    automargin=True
                )

                fig_temp.update_layout(
                    height=500,
                    margin=dict(b=125)
                )

                st.plotly_chart(
                    fig_temp,
                    width="stretch"
                )

            with tab2:
                fig_humidity = px.line(
                    df,
                    x="time",
                    y="relative_humidity_2m",
                    title="Páratartalom alakulása",
                    labels={
                        "time": "Időpont",
                        "relative_humidity_2m": "Páratartalom (%)"
                    },
                    markers=False
                )

                fig_humidity.update_xaxes(
                    tickmode="linear",
                    tick0=df["time"].min().normalize(),
                    dtick=4 * 60 * 60 * 1000,
                    tickformat="%m.%d %H:%M",
                    tickangle=-90,
                    side="bottom",
                    automargin=True
                )

                fig_humidity.update_layout(
                    height=500,
                    margin=dict(b=125)
                )

                st.plotly_chart(
                    fig_humidity,
                    width="stretch"
                )

            st.caption(
                f"Az előrejelzés {len(df)} órás adatpontot tartalmaz."
            )

        else:
            st.warning("Nem érkeztek óránkénti adatok.")

        st.caption("Időjárásadatok: Open-Meteo")


# 9. Keresési előzmények
st.divider()
st.subheader("📚 Keresési előzmények")

history_df = load_weather_history()

if not history_df.empty:
    history_df["searched_at"] = (
        pd.to_datetime(history_df["searched_at"], utc=True)
        .dt.tz_convert("Europe/Budapest")
        .dt.strftime("%Y-%m-%d %H:%M")
    )

    history_df = history_df.rename(columns={
        "city": "Város",
        "country": "Ország",
        "temperature": "Hőmérséklet (°C)",
        "humidity": "Páratartalom (%)",
        "wind_speed": "Szélsebesség (km/h)",
        "searched_at": "Lekérdezés ideje"
    })

    st.dataframe(
        history_df,
        hide_index=True,
        width="stretch"
    )
else:
    st.info("Még nincsenek mentett keresések.")
