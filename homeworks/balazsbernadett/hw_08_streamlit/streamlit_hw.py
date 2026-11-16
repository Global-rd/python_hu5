import streamlit as st
import plotly.express as px
import pandas as pd
import requests



def fetch_city(city_name):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            return data["results"][0]
    return None


@st.cache_data(ttl=1800, show_spinner="Fetching data...")
def fetch_weather(lat, lon):
    url = ( 
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
        f"&hourly=temperature_2m&forecast_days=5"
        )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def main():
    st.title("Robot Dreams Python - Weather Map & Data Visualization App")
    st.caption("Enter City Name")

    with st.form("city_form"):
        city_name = st.text_input(
            "Enter city name"
        )
        submitted = st.form_submit_button("Submit")
    if submitted:
        st.session_state.city_name = city_name
    if "city_name" not in st.session_state:
        st.session_state.city_name = "Budapest"

    data = fetch_city(st.session_state.city_name)
    if data is None:
        st.warning("There is no such city")
    else:
        lat = data["latitude"]
        lon = data["longitude"]
        country = data.get("country", "")
        exact_name = data["name"]

        weather_data = fetch_weather(lat, lon)

        if weather_data is None:
            st.warning("Somehing wrong")
        else:
            st.header(f"Current Weather in {exact_name}, {country}")
            current = weather_data["current"]
            kpi_temp, kpi_hum, kpi_wind = st.columns(3)

            with kpi_temp:
                st.metric(
                    label="Temperature (°C)",
                    value=f"{current['temperature_2m']}°C"
                )

            with kpi_hum:
                st.metric(
                    label="Humidity (%)",
                    value=f"{current['relative_humidity_2m']}%"
                )

            with kpi_wind:
                st.metric(
                    label="Wind Speed (km/h)",
                    value=f"{current['wind_speed_10m']} km/h"
                )

            st.subheader("Weather Map")
            map_df = pd.DataFrame({"lat": [lat], "lon": [lon]})
            st.map(map_df)


            df = pd.DataFrame({
              "Time": pd.to_datetime(weather_data["hourly"]["time"]),
              "Temperature (°C)": weather_data["hourly"]["temperature_2m"]
            })
            #st.write(df)


            st.subheader("Hourly Temperature Forecast (Next 5 days)")
            fig_close = px.line (
                df,
                x = "Time",
                y = "Temperature (°C)"
            )
            st.plotly_chart(fig_close)

if __name__ == "__main__":
    main()