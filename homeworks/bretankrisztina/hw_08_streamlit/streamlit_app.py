import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Weather Dashboard",
    page_icon="🌤️",
    layout="wide")

# API endpoints
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

# Get cities from Geocoding API
@st.cache_data(ttl=3600)
def find_cities(city_name):
    params = {
        "name": city_name,
        "count": 10,
        "language": "en",
        "format": "json"
    }
    response = requests.get(
        GEOCODING_URL,
        params=params,
        timeout=30
    )
    response.raise_for_status()
    data = response.json()
    return data.get("results", [])

# Format city names
def city_label(city):
    name = city.get("name", "")
    country = city.get("country", "")
    admin = city.get("admin1", "")

    if admin:
        return f"{name}, {admin}, {country}"
    return f"{name}, {country}"

# Get weather data
@st.cache_data(ttl=900)
def get_weather(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "wind_speed_10m"
        ],
        "hourly": [
            "temperature_2m",
            "relative_humidity_2m",
            "wind_speed_10m"
        ],
        "forecast_days": 5,
        "timezone": "auto"
    }
    response = requests.get(
        FORECAST_URL,
        params=params,
        timeout=30
    )
    response.raise_for_status()
    return response.json()

# Create forecast chart
def draw_forecast(df, column, label, color):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df[column],
            mode="lines",
            name=label,
            line=dict(
                color=color,
                width=2
            )
        )
    )
    fig.update_layout(
        template="plotly_dark",
        height=400,
        showlegend=False,
        xaxis_title=None,
        yaxis_title=None,
        xaxis=dict(
        tickformat="%m-%d %H:%M",
        tickangle=-90,
        dtick=4 * 60 * 60 * 1000,
        ticklabelmode="instant"
    ),
    margin=dict(l=0, r=0, t=10, b=80)
)
    st.plotly_chart(fig,use_container_width=True)

# Dashboard title
st.title(
    "Robot Dreams Python - Weather Map & Data Visualization App")

# City input
city_name = st.text_input("Enter city name",value="Budapest")

if city_name.strip():
    try:
        # Search for cities
        cities = find_cities(city_name.strip())
        if not cities:
            st.warning("No cities found. Please enter another city name.")
            st.stop()

        # Select the first matching city
        selected_city = cities[0]
        latitude = selected_city["latitude"]
        longitude = selected_city["longitude"]
        city = selected_city["name"]
        country = selected_city["country"]

        # Get weather
        weather_data = get_weather(latitude,longitude)
        current = weather_data["current"]
        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        wind_speed = current["wind_speed_10m"]

        # Current weather
        st.header(f"Current Weather in {city}, {country}")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Temperature (°C)",f"{temperature:.1f} °C")
        with col2:
            st.metric("Humidity (%)",f"{humidity}%")
        with col3:
            st.metric("Wind Speed (km/h)",f"{wind_speed:.1f} km/h")

        # Weather map
        st.subheader("Weather Map")
        map_df = pd.DataFrame({
            "latitude": [latitude],
            "longitude": [longitude]})
        st.map(
            map_df,
            latitude="latitude",
            longitude="longitude",
            zoom=10,
            size=90,
            color="#f04438")

        # Hourly forecast
        hourly = weather_data["hourly"]
        df = pd.DataFrame({
            "Time": pd.to_datetime(hourly["time"]),
            "Temperature": hourly["temperature_2m"],
            "Humidity": hourly["relative_humidity_2m"],
            "Wind Speed": hourly["wind_speed_10m"]})

        # Temperature chart
        st.subheader("Hourly Temperature Forecast (Next 5 Days)")
        draw_forecast(
            df,
            "Temperature",
            "Temperature (°C)",
            "#79C7FF")

        # Additional charts
        with st.expander("Additional Forecast Charts"):
            st.subheader("Hourly Humidity Forecast")
            draw_forecast(
                df,
                "Humidity",
                "Humidity (%)",
                "#63D2B3")

            st.subheader("Hourly Wind Speed Forecast")
            draw_forecast(
                df,
                "Wind Speed",
                "Wind Speed (km/h)",
                "#FFB86C")

        # Data table
        with st.expander("Hourly Weather Data"):
            st.dataframe(df,use_container_width=True)

    except requests.exceptions.RequestException as error:
        st.warning(f"API request failed: {error}")

    except (KeyError, ValueError, TypeError) as error:
        st.warning(f"Unable to process weather data: {error}")
else:
    st.warning("Please enter a city name.")