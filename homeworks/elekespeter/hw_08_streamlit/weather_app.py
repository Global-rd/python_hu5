import sqlite3
from datetime import datetime
from pathlib import Path

import pandas as pd
import plotly.express as px
import requests
import streamlit as st

from db_connector import SqliteDb

# =============================================================================
# KONSTANSOK
# =============================================================================
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
DEFAULT_CITY = "Budapest"
FORECAST_DAYS = 5

# EXTRA 2: az adatbázis a weather_app.py mellé kerül, bárhonnan is indítjuk
DB_PATH = Path(__file__).parent / "weather_searches.db"
TABLE_NAME = "searches"
CREATE_TABLE_QUERY = f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        city        TEXT,
        temperature REAL,
        humidity    REAL,
        wind_speed  REAL,
        searched_at TEXT
    )
"""


# =============================================================================
# 1. LÉPÉS: GEOCODING - városnévből koordináták
# =============================================================================
# A @st.cache_data miatt ugyanarra a városra nem hívjuk újra az API-t,
# amikor a Streamlit (minden interakciónál) újrafuttatja a szkriptet.
# Hibát (exception) nem tárol el, így egy sikertelen hívás később újrapróbálható.

@st.cache_data(ttl=3600, show_spinner="Searching for the city...")
def geocode_city(city_name: str) -> dict | None:
    """
    Megkeresi a várost a geocoding API-ban.
    Visszaadja a nevét, országát és koordinátáit, vagy None-t, ha nincs találat.
    API-hiba esetén requests.exceptions.RequestException-t dob.
    """
    params = {
        "name": city_name,
        "count": 1,          # csak a legjobb találat kell
        "language": "en",
        "format": "json",
    }
    response = requests.get(GEOCODING_URL, params=params, timeout=10)
    response.raise_for_status()

    # Ha nincs találat, a válaszban nincs "results" kulcs -> .get() None-t ad
    results = response.json().get("results")
    if not results:
        return None

    best_match = results[0]
    return {
        "name": best_match["name"],
        "country": best_match.get("country", ""),
        "lat": best_match["latitude"],
        "lon": best_match["longitude"],
    }


# =============================================================================
# 2. LÉPÉS: FORECAST - koordinátákból időjárás
# =============================================================================

@st.cache_data(ttl=600, show_spinner="Fetching weather data...")
def fetch_weather(lat: float, lon: float) -> dict:
    """
    Lekéri a jelenlegi időjárást és az óránkénti hőmérséklet-előrejelzést
    a megadott koordinátákra.
    API-hiba esetén requests.exceptions.RequestException-t dob.
    """
    params = {
        "latitude": lat,
        "longitude": lon,
        # a 3 KPI: hőmérséklet (°C), páratartalom (%), szélsebesség (km/h)
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        # EXTRA 1: óránkénti hőmérséklet a következő 5 napra
        "hourly": "temperature_2m",
        "forecast_days": FORECAST_DAYS,
        "timezone": "auto",  # a város helyi ideje
    }
    response = requests.get(FORECAST_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


# =============================================================================
# 3. LÉPÉS: MEGJELENÍTÉS (lesson_16/stock_dashboard.py alapján)
# =============================================================================

def show_kpis(current: dict) -> None:
    """A 3 KPI egymás mellett, 3 oszlopban."""
    col_temp, col_humidity, col_wind = st.columns(3)

    with col_temp:
        st.metric(label="Temperature (°C)", value=f"{current['temperature_2m']:.1f}°C")
    with col_humidity:
        st.metric(label="Humidity (%)", value=f"{current['relative_humidity_2m']:.0f}%")
    with col_wind:
        st.metric(label="Wind Speed (km/h)", value=f"{current['wind_speed_10m']:.1f} km/h")


def show_map(lat: float, lon: float) -> None:
    """Térkép a városra. Az st.map egy lat/lon oszlopos DataFrame-et vár."""
    st.subheader("Weather Map")
    location_df = pd.DataFrame({"lat": [lat], "lon": [lon]})
    st.map(location_df, zoom=10)


def show_forecast_chart(hourly: dict) -> None:
    """
    EXTRA 1: óránkénti hőmérséklet-előrejelzés vonaldiagramon
    (lesson_16/stock_dashboard.py: px.line + st.plotly_chart).
    Az API két párhuzamos listát ad: "time" (időpontok) és "temperature_2m".
    """
    forecast_df = pd.DataFrame({
        "Time": pd.to_datetime(hourly["time"]),
        "Temperature (°C)": hourly["temperature_2m"],
    })

    st.subheader(f"Hourly Temperature Forecast (Next {FORECAST_DAYS} Days)")
    fig = px.line(forecast_df, x="Time", y="Temperature (°C)")
    fig.update_xaxes(dtick=4 * 60 * 60 * 1000, tickformat="%m.%d %H:%M", tickangle=-90)  # 4 óránként
    st.plotly_chart(fig, width="stretch")


# =============================================================================
# 4. LÉPÉS: EXTRA 2 - keresések naplózása SQLite-ba (lesson_15/db_connector.py)
# =============================================================================

def log_search(place: str, current: dict) -> None:
    """
    Elmenti a keresést az adatbázisba.
    A Streamlit minden interakciónál újrafuttatja a szkriptet, ezért a
    session_state-ben megjegyezzük az utoljára mentett helyet, és csak akkor
    írunk az adatbázisba, ha a felhasználó új várost keresett.
    """
    if st.session_state.get("last_logged_place") == place:
        return

    record = {
        "city": place,
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"],
        "searched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    try:
        with SqliteDb(DB_PATH) as db:
            db.create_table(CREATE_TABLE_QUERY)
            db.write_single_record(TABLE_NAME, record)
        st.session_state["last_logged_place"] = place
    except (RuntimeError, sqlite3.Error) as e:
        # Az adatbázis hibája ne állítsa le az appot, csak jelezzük.
        st.warning(f"The search could not be saved to the database: {e}")


def show_search_history(limit: int = 10) -> None:
    """Az utolsó keresések táblázata az adatbázisból (select_records)."""
    st.subheader("Recent Searches")
    try:
        with SqliteDb(DB_PATH) as db:
            db.create_table(CREATE_TABLE_QUERY)
            history_df = db.select_records(
                f"SELECT * FROM {TABLE_NAME} ORDER BY searched_at DESC LIMIT {limit}"
            )
    except (RuntimeError, sqlite3.Error) as e:
        st.warning(f"The search history could not be loaded: {e}")
        return

    if history_df.empty:
        st.info("No searches have been saved yet.")
    else:
        st.dataframe(history_df, hide_index=True, width="stretch")


# =============================================================================
# FŐPROGRAM
# =============================================================================

def main():
    st.set_page_config(page_title="Weather App", page_icon="🌤️")
    st.title("Robot Dreams Python - Weather Map & Data Visualization App")

    # 1. A felhasználó megadja a városnevet
    city_input = st.text_input("Enter city name", DEFAULT_CITY).strip()
    if not city_input:
        st.info("Please enter a city name.")
        st.stop()

    # 2. Geocoding: városnév -> lat, lon
    try:
        location = geocode_city(city_input)
    except requests.exceptions.RequestException as e:
        st.warning(f"The city search service is not available right now: {e}")
        st.stop()

    if location is None:
        st.warning(f"No city found with the name '{city_input}'. Please check the spelling.")
        st.stop()

    # 3. Forecast: lat, lon -> időjárás
    try:
        weather = fetch_weather(location["lat"], location["lon"])
    except requests.exceptions.RequestException as e:
        st.warning(f"The weather service is not available right now: {e}")
        st.stop()

    current = weather.get("current")
    if not current:
        st.warning("The weather service returned no current data for this location.")
        st.stop()

    # 4. Megjelenítés - minden városnévvel kapcsolatos szöveg dinamikus
    place = f"{location['name']}, {location['country']}" if location["country"] else location["name"]
    st.header(f"Current Weather in {place}")
    show_kpis(current)
    show_map(location["lat"], location["lon"])

    hourly = weather.get("hourly")
    if hourly:
        show_forecast_chart(hourly)
    else:
        st.warning("No hourly forecast data is available for this location.")

    # EXTRA 2: naplózás és a keresési előzmények
    log_search(place, current)
    show_search_history()


main()
