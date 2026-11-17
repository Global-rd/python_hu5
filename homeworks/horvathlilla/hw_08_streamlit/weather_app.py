

import pandas as pd
import requests
import streamlit as st

st.set_page_config(page_title="Weather Map and Data Visualisation App", page_icon="☀️", layout="wide")
st.title("Weather Map and Data Visualisation App")

GEOCODING_API = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_API = "https://api.open-meteo.com/v1/forecast"


@st.cache_data(ttl=3600)
def geocode_city(city_name: str):
    params = {
        "name": city_name,
        "count": 1,
        "language": "en",
        "format": "json",
    }
    response = requests.get(GEOCODING_API, params=params, timeout=10)
    response.raise_for_status()
    payload = response.json()

    if not payload.get("results"):
        raise ValueError(f"No city found for '{city_name}'.")

    result = payload["results"][0]
    return {
        "name": result.get("name", city_name),
        "country": result.get("country", "Unknown country"),
        "admin1": result.get("admin1", ""),
        "latitude": result.get("latitude"),
        "longitude": result.get("longitude"),
        "timezone": result.get("timezone", "auto"),
    }


@st.cache_data(ttl=3600)
def get_forecast(latitude: float, longitude: float):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "hourly": "temperature_2m,relative_humidity_2m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
        "timezone": "auto",
        "forecast_days": 7,
    }
    response = requests.get(FORECAST_API, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


st.header("City lookup")
city_input = st.text_input("Enter a city name", value="", placeholder="e.g. Budapest")


if st.button("Search"):
    city_name = city_input.strip()
    if not city_name:
        st.warning("Please provide a valid city name.")
        st.stop()

    try:
        location = geocode_city(city_name)
    except requests.RequestException as exc:
        st.warning(f"API request error while looking up city: {exc}")
        st.stop()
    except ValueError as exc:
        st.warning(str(exc))
        st.stop()

    country = location["country"]
    admin1 = location["admin1"]
    st.title(f"{location['name']}, {country}")
    st.caption(f"Region: {admin1} • Timezone: {location['timezone']}")

    try:
        weather = get_forecast(location["latitude"], location["longitude"])
    except requests.RequestException as exc:
        st.warning(f"API request error while fetching weather data: {exc}")
        st.stop()

    current = weather.get("current", {})
    hourly = weather.get("hourly", {})
    daily = weather.get("daily", {})

    temperature = current.get("temperature_2m")
    humidity = current.get("relative_humidity_2m")
    wind_speed = current.get("wind_speed_10m")

    if temperature is None or humidity is None or wind_speed is None:
        st.warning("The selected city does not have complete weather data available right now.")
        st.stop()

    kpi_temperature, kpi_humidity, kpi_wind_speed = st.columns(3)

    with kpi_temperature:
        st.metric("Temperature", f"{temperature:.1f}°C")

    with kpi_humidity:
        st.metric("Humidity", f"{humidity:.0f}%")

    with kpi_wind_speed:
        st.metric("Wind speed", f"{wind_speed:.1f} km/h")

    if hourly.get("time"):
        hourly_df = pd.DataFrame(
            {
                "time": hourly["time"][:24],
                "temperature": hourly.get("temperature_2m", [])[:24],
                "humidity": hourly.get("relative_humidity_2m", [])[:24],
            }
        )
        hourly_df["time"] = pd.to_datetime(hourly_df["time"])
        hourly_df = hourly_df.set_index("time")

        tab_temp, tab_humidity, tab_daily = st.tabs(["Temperature", "Humidity", "7-day overview"])

        with tab_temp:
            st.line_chart(hourly_df[["temperature"]], use_container_width=True)

        with tab_humidity:
            st.line_chart(hourly_df[["humidity"]], use_container_width=True)

        with tab_daily:
            if daily.get("time"):
                daily_df = pd.DataFrame(
                    {
                        "date": daily.get("time", []),
                        "max_temp": daily.get("temperature_2m_max", []),
                        "min_temp": daily.get("temperature_2m_min", []),
                        "precipitation_probability": daily.get("precipitation_probability_max", []),
                    }
                )
                daily_df["date"] = pd.to_datetime(daily_df["date"])
                st.line_chart(daily_df.set_index("date")[["max_temp", "min_temp"]], use_container_width=True)
                st.dataframe(daily_df, use_container_width=True)

    else:
        st.info("No hourly forecast data was returned for this location.")

else:
    st.info("Choose a city and press Search to see current weather and trends.")
    st.stop()

st.header("Weather Map")
map_center = [location["latitude"], location["longitude"]]
st.map(data=pd.DataFrame({"lat": [map_center[0]], "lon": [map_center[1]]}), zoom=10, use_container_width=True)
