import datetime
from pathlib import Path

import pandas as pd
import plotly.express as px
import requests
import streamlit as st

from db_connector import SqliteDb

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

#az adatbázis a script mellé kerül, bárhonnan indítjuk a streamlit run-t
DB_PATH = Path(__file__).parent / "weather_searches.db"
TABLE_NAME = "searches"

CREATE_TABLE_QUERY = f"""
CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
    city TEXT,
    temperature REAL,
    humidity REAL,
    wind_speed REAL,
    searched_at TEXT
)
"""


@st.cache_data(ttl=3600, show_spinner="Searching city...")
def fetch_location(city_name):
    """1-2. lépés: városnév -> lat/lon (+ név és ország a kiíráshoz). None, ha nincs ilyen város."""
    parameters = {"name": city_name, "count": 1, "language": "en", "format": "json"}
    response = requests.get(url=GEOCODING_URL, params=parameters, timeout=10)
    response.raise_for_status()
    results = response.json().get("results")

    if not results:
        return None

    location = results[0]
    return {"name": location["name"],
            "country": location.get("country", ""),
            "lat": location["latitude"],
            "lon": location["longitude"]}


@st.cache_data(ttl=600, show_spinner="Fetching weather data...")
def fetch_weather(lat, lon):
    """3. lépés: lat/lon -> jelenlegi időjárás + óránkénti hőmérséklet-előrejelzés 5 napra."""
    parameters = {"latitude": lat,
                  "longitude": lon,
                  "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
                  "hourly": "temperature_2m",
                  "forecast_days": 5,
                  "timezone": "auto"}
    response = requests.get(url=FORECAST_URL, params=parameters, timeout=10)
    response.raise_for_status()
    return response.json()


def process_forecast(data):
    """Az óránkénti előrejelzésből DataFrame-et készít a charthoz."""
    df = pd.DataFrame({"time": pd.to_datetime(data["hourly"]["time"]),
                       "temperature": data["hourly"]["temperature_2m"]})
    return df


def log_search(city, current):
    """EXTRA 2: minden keresés naplózása az sqlite adatbázisba."""
    record = {"city": city,
              "temperature": current["temperature_2m"],
              "humidity": current["relative_humidity_2m"],
              "wind_speed": current["wind_speed_10m"],
              "searched_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

    with SqliteDb(DB_PATH) as db:
        db.create_table(CREATE_TABLE_QUERY)
        db.write_single_record(TABLE_NAME, record)


def read_search_log():
    with SqliteDb(DB_PATH) as db:
        db.create_table(CREATE_TABLE_QUERY)
        return db.select_records(f"SELECT * FROM {TABLE_NAME} ORDER BY searched_at DESC")


def main():
    st.set_page_config(page_title="Weather App", page_icon="🌤️")
    st.title("Robot Dreams Python - Weather Map & Data Visualization App")

    with st.form("city_form"):
        city_input = st.text_input("Enter city name", "Budapest")
        submitted = st.form_submit_button("Search")

    if not city_input.strip():
        st.warning("Please enter a city name.")
        return

    try:
        location = fetch_location(city_input.strip())
    except requests.RequestException as e:
        st.warning(f"Geocoding API error: {e}")
        return

    if location is None:
        st.warning(f"City not found: {city_input}")
        return

    try:
        weather = fetch_weather(location["lat"], location["lon"])
    except requests.RequestException as e:
        st.warning(f"Forecast API error: {e}")
        return

    current = weather["current"]
    place = f"{location['name']}, {location['country']}" if location["country"] else location["name"]

    #csak a Search gombra naplózunk (a többi újrafuttatás pl. tabváltás nem új keresés)
    if submitted:
        log_search(place, current)

    #4. lépés: megjelenítés
    st.header(f"Current Weather in {place}")

    kpi_temp, kpi_humidity, kpi_wind = st.columns(3)
    with kpi_temp:
        st.metric(label="Temperature (°C)", value=f"{current['temperature_2m']}°C")
    with kpi_humidity:
        st.metric(label="Humidity (%)", value=f"{current['relative_humidity_2m']}%")
    with kpi_wind:
        st.metric(label="Wind Speed (km/h)", value=f"{current['wind_speed_10m']} km/h")

    tab_map, tab_forecast, tab_log = st.tabs(["Weather Map", "Forecast", "Search log"])

    with tab_map:
        st.subheader(f"Weather Map - {place}")
        st.map(pd.DataFrame({"lat": [location["lat"]], "lon": [location["lon"]]}), zoom=9)

    #EXTRA 1: óránkénti hőmérséklet-előrejelzés
    with tab_forecast:
        st.subheader(f"Hourly Temperature Forecast (Next 5 Days) - {place}")
        forecast_df = process_forecast(weather)
        fig = px.line(forecast_df, x="time", y="temperature",
                      labels={"time": "Time", "temperature": "Temperature (°C)"})
        st.plotly_chart(fig)

    with tab_log:
        st.subheader("Search log (sqlite)")
        st.dataframe(read_search_log(), hide_index=True)


if __name__ == "__main__":
    main()
