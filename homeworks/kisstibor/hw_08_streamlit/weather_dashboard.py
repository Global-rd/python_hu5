import datetime
import sqlite3
from pathlib import Path

import pandas as pd
import plotly.express as px
import requests
import streamlit as st


# A két API-cím és a helyi adatbázis elérési útja.
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
DB_PATH = Path(__file__).parent / "weather_searches.db"


def get_location(city):
    """Megkeresi a város első találatát és koordinátáit."""
    params = {"name": city, "count": 1, "language": "hu", "format": "json"}

    # A válasz JSON adatait Python-szótárrá alakítjuk.
    try:
        response = requests.get(GEOCODING_URL, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException:
        st.warning("Nem sikerült elérni a településkereső szolgáltatást.")
        return None
    except ValueError:
        st.warning("A településkereső hibás választ adott.")
        return None

    if "results" not in data or not data["results"]:
        st.warning("Nem találtam ilyen települést. Próbálj másik nevet.")
        return None

    # Az első találatot használjuk, ha minden adat megvan.
    location = data["results"][0]
    if not all(key in location for key in ["name", "country", "latitude", "longitude"]):
        st.warning("A település adatai hiányosak.")
        return None

    return location


def get_weather(latitude, longitude):
    """Lekéri a jelenlegi időjárást és az óránkénti előrejelzést."""
    # Hat naptári napból az aktuális órától öt napot tudunk kiválasztani.
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "hourly": "temperature_2m",
        "forecast_days": 6,
        "timezone": "auto",
        "wind_speed_unit": "kmh",
    }

    try:
        response = requests.get(FORECAST_URL, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException:
        st.warning("Nem sikerült lekérni az időjárási adatokat.")
        return None
    except ValueError:
        st.warning("Az időjárási szolgáltatás hibás választ adott.")
        return None

    if "current" not in data:
        st.warning("A jelenlegi időjárási adatok nem érhetők el.")
        return None

    # Ellenőrizzük a mutatókhoz szükséges mezőket.
    current = data["current"]
    required = ["temperature_2m", "relative_humidity_2m", "wind_speed_10m", "time"]
    if not all(key in current and current[key] is not None for key in required):
        st.warning("A jelenlegi időjárási adatok hiányosak.")
        return None

    return data


# Extra feladat 2: a sikeres időjárás-keresések mentése SQLite adatbázisba.
def save_search(city, temperature, humidity, wind_speed):
    """Elment a sikeres keresést a helyi SQLite adatbázisba."""
    connection = sqlite3.connect(DB_PATH)
    try:
        # A módosítást véglegesíti, hiba esetén visszavonja a módosítást.
        with connection:
            # A kérdőjelek helyére az értékek kerülnek be.
            connection.execute(
                """CREATE TABLE IF NOT EXISTS searches (
                    city TEXT,
                    temperature REAL,
                    humidity REAL,
                    wind_speed REAL,
                    search_time TEXT
                )"""
            )
            connection.execute(
                "INSERT INTO searches VALUES (?, ?, ?, ?, ?)",
                (city, temperature, humidity, wind_speed, datetime.datetime.now().isoformat()),
            )
    finally:
        # A kapcsolatot hiba esetén is bezárjuk.
        connection.close()


def main():
    """Megjeleníti a felületet, és kezeli a városkeresést."""
    st.title("Időjárás dashboard")

    # Az űrlap tartalmát a Keresés gomb küldi be.
    with st.form("city_form"):
        city = st.text_input("Add meg a város nevét")
        submitted = st.form_submit_button("Keresés")

    if submitted:
        # Új kereséskor töröljük az előző eredményt.
        st.session_state.pop("weather", None)
        st.session_state.pop("location", None)

        if len(city.strip()) < 2:
            st.warning("Legalább két karakterből álló városnevet adj meg.")
        else:
            location = get_location(city.strip())
            if location is not None:
                weather = get_weather(location["latitude"], location["longitude"])
                if weather is not None:
                    # A munkamenetben az újrafuttatások között is megmarad az eredmény.
                    st.session_state.location = location
                    st.session_state.weather = weather

                    # Extra feladat 2: egyszeri mentés minden sikeres kereséskor.
                    current = weather["current"]
                    city_name = f'{location["name"]}, {location["country"]}'
                    try:
                        save_search(
                            city_name,
                            current["temperature_2m"],
                            current["relative_humidity_2m"],
                            current["wind_speed_10m"],
                        )
                    except sqlite3.Error:
                        st.warning("Az időjárás megjeleníthető, de a keresés mentése nem sikerült.")

    if "weather" in st.session_state:
        location = st.session_state.location
        weather = st.session_state.weather
        current = weather["current"]
        city_name = f'{location["name"]}, {location["country"]}'

        st.header(f"Jelenlegi időjárás: {city_name}")
        st.caption(f'Az adat időpontja: {current["time"]} ({weather.get("timezone", "helyi idő")})')

        # A három mutatót egymás melletti oszlopokban jelenítjük meg.
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Hőmérséklet", f'{current["temperature_2m"]} °C')
        with col2:
            st.metric("Páratartalom", f'{current["relative_humidity_2m"]} %')
        with col3:
            st.metric("Szélsebesség", f'{current["wind_speed_10m"]} km/h')

        # A térkép a keresett település koordinátáit használja.
        st.subheader(f"Térkép: {city_name}")
        map_data = pd.DataFrame({
            "lat": [location["latitude"]],
            "lon": [location["longitude"]],
        })
        st.map(map_data, zoom=9)

        # Extra feladat 1: a következő öt nap óránkénti hőmérsékletének diagramja.
        st.subheader(f"Óránkénti előrejelzés: {city_name}")
        hourly = weather.get("hourly", {})
        times = hourly.get("time", [])
        temperatures = hourly.get("temperature_2m", [])

        if times and len(times) == len(temperatures):
            # A dátumokat átalakítjuk, majd az aktuális órától 120 órát választunk ki.
            forecast_df = pd.DataFrame({"Időpont": times, "Hőmérséklet": temperatures})
            forecast_df["Időpont"] = pd.to_datetime(forecast_df["Időpont"], errors="coerce")
            current_time = pd.to_datetime(current["time"], errors="coerce")
            forecast_df = forecast_df[forecast_df["Időpont"] >= current_time.floor("h")]
            forecast_df = forecast_df.sort_values("Időpont").head(120)

            if not forecast_df.empty:
                fig = px.line(
                    forecast_df,
                    x="Időpont",
                    y="Hőmérséklet",
                    labels={"Hőmérséklet": "Hőmérséklet (°C)"},
                    title=f"Hőmérséklet a következő öt napban: {city_name}",
                )
                st.plotly_chart(fig)
            else:
                st.warning("Az óránkénti előrejelzés nem érhető el.")
        else:
            st.warning("Az óránkénti előrejelzés hiányos.")

    st.caption("Adatforrás: [Open-Meteo](https://open-meteo.com/) – CC BY 4.0")


if __name__ == "__main__":
    main()
