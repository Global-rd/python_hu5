"""A small weather dashboard powered by the Open-Meteo APIs."""

import json
import sqlite3
from datetime import datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import pandas as pd
import streamlit as st


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
DATABASE_FILE = Path(__file__).with_name("weather_searches.sqlite3")


class WeatherError(Exception):
    """A weather lookup could not be completed."""


def fetch_json(url: str, params: dict) -> dict:
    """Request JSON from an API and turn network errors into readable errors."""
    request = Request(f"{url}?{urlencode(params)}", headers={"User-Agent": "weather-homework/1.0"})
    try:
        with urlopen(request, timeout=10) as response:
            data = json.load(response)
    except (HTTPError, URLError, TimeoutError, OSError, ValueError) as exc:
        raise WeatherError("The weather service is unavailable. Please try again.") from exc

    if not isinstance(data, dict):
        raise WeatherError("The weather service returned invalid data.")
    if data.get("error"):
        raise WeatherError(data.get("reason", "The weather service returned an error."))
    return data


def find_city(city_name: str) -> dict:
    """Convert a city name to coordinates using the geocoding API."""
    data = fetch_json(GEOCODING_URL, {"name": city_name, "count": 5, "language": "en"})
    results = data.get("results") or []
    if not results:
        raise WeatherError("City not found. Try a more specific name, such as 'Paris, France'.")
    city = results[0]
    if not all(key in city for key in ("name", "country", "latitude", "longitude")):
        raise WeatherError("The city search returned incomplete location data.")
    return city


def get_weather(city: dict) -> dict:
    """Get current conditions and five days of hourly temperature values."""
    data = fetch_json(
        FORECAST_URL,
        {
            "latitude": city["latitude"],
            "longitude": city["longitude"],
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
            "hourly": "temperature_2m",
            "forecast_days": 5,
            "timezone": "auto",
        },
    )
    current = data.get("current") or {}
    hourly = data.get("hourly") or {}
    if not all(key in current for key in ("temperature_2m", "relative_humidity_2m", "wind_speed_10m")):
        raise WeatherError("The weather service returned incomplete current conditions.")
    if not hourly.get("time") or len(hourly["time"]) != len(hourly.get("temperature_2m", [])):
        raise WeatherError("The weather service returned incomplete forecast data.")
    return data


def log_search(city: str, current: dict) -> None:
    """Save one successful search in a local SQLite database."""
    with sqlite3.connect(DATABASE_FILE) as connection:
        connection.execute(
            """CREATE TABLE IF NOT EXISTS weather_searches (
                city TEXT NOT NULL,
                temperature REAL NOT NULL,
                humidity REAL NOT NULL,
                wind_speed REAL NOT NULL,
                searched_at TEXT NOT NULL
            )"""
        )
        connection.execute(
            """INSERT INTO weather_searches
               (city, temperature, humidity, wind_speed, searched_at)
               VALUES (?, ?, ?, ?, ?)""",
            (
                city,
                current["temperature_2m"],
                current["relative_humidity_2m"],
                current["wind_speed_10m"],
                datetime.now().isoformat(timespec="seconds"),
            ),
        )


def main() -> None:
    st.set_page_config(page_title="Weather dashboard", page_icon="☀️", layout="wide")
    st.title("Weather dashboard")
    st.caption("Current conditions and a five-day forecast from Open-Meteo")

    with st.form("city_search"):
        city_name = st.text_input("Enter a city", value="Diósd", placeholder="e.g. Paris, France")
        search = st.form_submit_button("Show weather")

    if search:
        if not city_name.strip():
            st.warning("Please enter a city name.")
        else:
            try:
                city = find_city(city_name.strip())
                weather = get_weather(city)
                st.session_state["result"] = (city, weather)
                try:
                    log_search(f"{city['name']}, {city['country']}", weather["current"])
                except sqlite3.Error:
                    st.warning("Weather loaded, but this search could not be saved locally.")
            except WeatherError as exc:
                st.session_state.pop("result", None)
                st.warning(str(exc))

    if "result" not in st.session_state:
        st.info("Enter a city and select Show weather to begin.")
        return

    city, weather = st.session_state["result"]
    current = weather["current"]
    label = f"{city['name']}, {city['country']}"
    st.subheader(f"Current weather in {label}")

    temperature_col, humidity_col, wind_col = st.columns(3)
    temperature_col.metric("Temperature", f"{current['temperature_2m']:.1f} °C")
    humidity_col.metric("Humidity", f"{current['relative_humidity_2m']:.0f} %")
    wind_col.metric("Wind speed", f"{current['wind_speed_10m']:.1f} km/h")

    st.subheader(f"Weather map: {label}")
    map_data = pd.DataFrame([{"lat": city["latitude"], "lon": city["longitude"]}])
    st.map(map_data, zoom=10)

    st.subheader(f"Hourly temperature forecast for {label} (next 5 days)")
    forecast = pd.DataFrame(
        {
            "Time": pd.to_datetime(weather["hourly"]["time"]),
            "Temperature (°C)": weather["hourly"]["temperature_2m"],
        }
    )
    st.line_chart(forecast, x="Time", y="Temperature (°C)", x_label="Local time", y_label="°C")
    st.caption("Weather data: Open-Meteo. Search history is saved in a local SQLite file.")


if __name__ == "__main__":
    main()
