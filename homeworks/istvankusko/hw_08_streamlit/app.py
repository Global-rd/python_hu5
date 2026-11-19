

from pathlib import Path
import sys

import streamlit as st

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from weather_utils import (
    build_hourly_forecast_df,
    fetch_weather_forecast,
    geocode_city,
    init_db,
    log_search,
    render_current_weather_kpis,
    render_forecast_chart,
    render_search_logs,
    render_weather_map,
)


def main() -> None:
    """Run the Streamlit Weather Map & Data Visualization App."""
    st.set_page_config(
        page_title="Robot Dreams Python - Weather Map & Data Visualization App",
        layout="wide",
    )

    init_db()

    st.title("Robot Dreams Python - Weather Map & Data Visualization App")

    city_input = st.text_input("Enter city name", value="Diósd")

    if not city_input.strip():
        st.info("Please enter a city name to view weather data.")
        render_search_logs()
        return

    location = geocode_city(city_input)
    if not location:
        render_search_logs()
        return

    lat = location["latitude"]
    lon = location["longitude"]
    resolved_city = location["name"]
    country = location["country"]
    location_label = f"{resolved_city}, {country}"

    forecast_data = fetch_weather_forecast(lat, lon)
    if not forecast_data:
        render_search_logs()
        return

    current_data = forecast_data.get("current", {})
    temp = current_data.get("temperature_2m")
    humidity = current_data.get("relative_humidity_2m")
    wind_speed = current_data.get("wind_speed_10m")

    log_key = f"{location_label}|{temp}|{humidity}|{wind_speed}"
    if st.session_state.get("last_logged_key") != log_key:
        log_search(
            city_name=location_label,
            temperature=temp,
            humidity=humidity,
            wind_speed=wind_speed,
        )
        st.session_state["last_logged_key"] = log_key

    render_current_weather_kpis(location_label, current_data)
    render_weather_map(lat, lon)

    forecast_df = build_hourly_forecast_df(forecast_data)
    render_forecast_chart(forecast_df)
    render_search_logs()


if __name__ == "__main__":
    main()

