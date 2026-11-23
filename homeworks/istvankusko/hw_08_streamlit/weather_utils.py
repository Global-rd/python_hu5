

from datetime import datetime
import sqlite3
from typing import Any

import pandas as pd
import requests
import streamlit as st

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
DB_PATH = "weather_searches.db"


def init_db(db_path: str = DB_PATH) -> None:
    """Create the SQLite database and search_logs table if they do not exist."""
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS search_logs (
                city_name TEXT NOT NULL,
                temperature REAL,
                humidity REAL,
                wind_speed REAL,
                searched_at TEXT NOT NULL
            )
            """
        )
        conn.commit()


def log_search(
    city_name: str,
    temperature: float | None,
    humidity: float | None,
    wind_speed: float | None,
    db_path: str = DB_PATH,
) -> None:
    """Insert a search record with current timestamp into the SQLite table."""
    searched_at = datetime.now().isoformat(timespec="seconds")
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO search_logs (
                city_name,
                temperature,
                humidity,
                wind_speed,
                searched_at
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (city_name, temperature, humidity, wind_speed, searched_at),
        )
        conn.commit()


@st.cache_data(ttl=3600)
def geocode_city(city_name: str) -> dict[str, Any] | None:
    """Fetch latitude, longitude, resolved city name, and country from Open-Meteo Geocoding API."""
    params = {
        "name": city_name.strip(),
        "count": 1,
        "language": "en",
        "format": "json",
    }
    try:
        response = requests.get(GEOCODING_URL, params=params, timeout=10)
        response.raise_for_status()
        payload = response.json()
    except requests.RequestException as exc:
        st.warning(f"Geocoding API request failed: {exc}")
        return None
    except ValueError as exc:
        st.warning(f"Failed to parse Geocoding API response: {exc}")
        return None

    results = payload.get("results")
    if not results:
        st.warning(f"No location found for '{city_name}'. Please try another city name.")
        return None

    top_result = results[0]
    return {
        "name": top_result.get("name", city_name.strip()),
        "country": top_result.get("country", "Unknown Country"),
        "latitude": top_result.get("latitude"),
        "longitude": top_result.get("longitude"),
    }


@st.cache_data(ttl=900)
def fetch_weather_forecast(latitude: float, longitude: float) -> dict[str, Any] | None:
    """Fetch current weather metrics and 5-day hourly temperature forecast from Open-Meteo."""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "hourly": "temperature_2m",
        "forecast_days": 5,
        "timezone": "auto",
    }
    try:
        response = requests.get(FORECAST_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        st.warning(f"Weather Forecast API request failed: {exc}")
        return None
    except ValueError as exc:
        st.warning(f"Failed to parse Weather Forecast API response: {exc}")
        return None


def build_hourly_forecast_df(forecast_data: dict[str, Any]) -> pd.DataFrame:
    """Convert hourly forecast payload into a clean DataFrame indexed by timestamp."""
    hourly = forecast_data.get("hourly", {})
    times = hourly.get("time", [])
    temperatures = hourly.get("temperature_2m", [])

    df = pd.DataFrame(
        {
            "Timestamp": pd.to_datetime(times),
            "Temperature (°C)": temperatures,
        }
    )
    if not df.empty:
        df["Formatted Time"] = df["Timestamp"].dt.strftime("%m.%d %H:%M")
        df = df.set_index("Formatted Time")
    return df


def render_current_weather_kpis(
    location_label: str, current_data: dict[str, Any]
) -> None:
    """Render key metric cards for current temperature, humidity, and wind speed."""
    st.subheader(f"Current Weather in {location_label}")

    temp = current_data.get("temperature_2m")
    humidity = current_data.get("relative_humidity_2m")
    wind_speed = current_data.get("wind_speed_10m")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            label="Temperature (°C)",
            value=f"{temp:.1f}°C" if temp is not None else "N/A",
        )
    with col2:
        st.metric(
            label="Humidity (%)",
            value=f"{humidity:.0f}%" if humidity is not None else "N/A",
        )
    with col3:
        st.metric(
            label="Wind Speed (km/h)",
            value=f"{wind_speed:.1f} km/h" if wind_speed is not None else "N/A",
        )


def render_weather_map(latitude: float, longitude: float) -> None:
    """Render a map centered on the selected location's coordinates."""
    st.subheader("Weather Map")
    map_df = pd.DataFrame({"lat": [latitude], "lon": [longitude]})
    st.map(map_df, zoom=10)


def render_forecast_chart(forecast_df: pd.DataFrame) -> None:
    """Render the 5-day hourly temperature forecast line chart."""
    st.subheader("Hourly Temperature Forecast (Next 5 Days)")
    if forecast_df.empty:
        st.warning("Hourly forecast data is unavailable for this location.")
        return
    st.line_chart(forecast_df["Temperature (°C)"])


def render_search_logs(db_path: str = DB_PATH) -> None:
    """Display recent logged searches from the SQLite database."""
    with st.expander("Recent Search Logs (SQLite)"):
        try:
            with sqlite3.connect(db_path) as conn:
                logs_df = pd.read_sql_query(
                    """
                    SELECT city_name, temperature, humidity, wind_speed, searched_at
                    FROM search_logs
                    ORDER BY rowid DESC
                    LIMIT 20
                    """,
                    conn,
                )
            if logs_df.empty:
                st.info("No searches logged yet.")
            else:
                st.dataframe(logs_df, use_container_width=True)
        except sqlite3.Error as exc:
            st.warning(f"Could not read search logs from SQLite: {exc}")

            