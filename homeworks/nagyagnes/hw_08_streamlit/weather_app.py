import streamlit as st
import requests
import pandas as pd

st.title("Weather Dashboard")

city = st.text_input("Enter city name:")

if city:
    st.write(f"Selected city: {city}")
    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    #response = requests.get(url, params=params)
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException:
        #st.error("City data could not be loaded.")
        st.warning("City data could not be loaded.")
        st.stop()
    if "results" not in data:
        st.warning("City not found. Please enter a valid city name.")
        st.stop()

    #st.write(data)
    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]
    country = data["results"][0]["country"]
    st.write(f"Latitude: {latitude}")
    st.write(f"Longitude: {longitude}")
    st.write(f"Country: {country}")

    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}

    #weather_response = requests.get(weather_url, params=weather_params)
    #weather_data = weather_response.json()

    try:
        weather_response = requests.get(
            weather_url,
                params=weather_params,
                timeout=10
        )
        weather_response.raise_for_status()
        weather_data = weather_response.json()

    except requests.exceptions.RequestException:
        #st.error("Weather data could not be loaded.")
        st.warning("Weather data could not be loaded.")
        st.stop()

    #st.write(weather_data)
    hourly_data = weather_data["hourly"]
    df = pd.DataFrame(hourly_data)
    df["time"] = pd.to_datetime(df["time"])

    st.write(df.head())
    st.subheader("Hourly Temperature")
    st.line_chart(df, x="time", y="temperature_2m")
    st.subheader("Hourly Humidity")
    st.line_chart(df, x="time", y="relative_humidity_2m")
    st.subheader("Hourly Wind Speed")
    st.line_chart(df, x="time", y="wind_speed_10m")
    temperature = weather_data["current"]["temperature_2m"]
    humidity = weather_data["current"]["relative_humidity_2m"]
    wind_speed = weather_data["current"]["wind_speed_10m"]

    #st.subheader(f"Current Weather in {city}, {country}")
    st.subheader(f"Current Weather in {city.title()}, {country}")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Temperature",
            value=f"{temperature} °C"
    )

    with col2:
        st.metric(
            label="Humidity",
            value=f"{humidity} %"
    )

    with col3:
        st.metric(
            label="Wind Speed",
            value=f"{wind_speed} km/h"
    )
        
    st.subheader("Weather Map")

    map_data = pd.DataFrame({
        "lat": [latitude],
        "lon": [longitude]
    })

    st.map(map_data)