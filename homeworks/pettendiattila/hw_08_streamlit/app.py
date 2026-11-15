
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import sqlite3
from datetime import datetime

st.title("Robot Dreams Python - Weather App")

st.header("Weather Dashboard")

st.write("Welcome to my weather application!")

city = st.text_input("Enter city name")

if city and st.button("Search"):

    try:
        url = "https://geocoding-api.open-meteo.com/v1/search"

        parameters = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        response = requests.get(url, params=parameters)

        data = response.json()

        if "results" in data and data["results"]:
            location = data["results"][0]

            latitude = location["latitude"]
            longitude = location["longitude"]

            st.write("City:", location["name"])
            st.write("Country:", location["country"])
            st.write("Latitude:", latitude)
            st.write("Longitude:", longitude)

            weather_url = "https://api.open-meteo.com/v1/forecast"

            weather_parameters = {
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
                "hourly": "temperature_2m",
                "forecast_days": 5
            }

            weather_response = requests.get(
                weather_url,
                params=weather_parameters
            )

            weather_data = weather_response.json()

            current_weather = weather_data["current"]

            temperature = current_weather["temperature_2m"]
            humidity = current_weather["relative_humidity_2m"]
            wind_speed = current_weather["wind_speed_10m"]

            st.subheader("Current Weather")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Temperature",
                str(temperature) + " °C"
            )

            col2.metric(
                "Humidity",
                str(humidity) + " %"
            )

            col3.metric(
                "Wind Speed",
                str(wind_speed) + " km/h"
            )

            st.subheader("Hourly Temperature Forecast (Next 5 Days)")

            forecast_data = weather_data["hourly"]

            df = pd.DataFrame({
                "Time": forecast_data["time"],
                "Temperature": forecast_data["temperature_2m"]
            })

            fig = px.line(
                df,
                x="Time",
                y="Temperature",
                title="Hourly Temperature Forecast"
            )

            st.plotly_chart(fig)

            conn = sqlite3.connect("weather.db")

            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO weather_logs
                (city, temperature, humidity, wind_speed, search_time)
                VALUES (?, ?, ?, ?, ?)
            """, (
                location["name"],
                temperature,
                humidity,
                wind_speed,
                datetime.now()
            ))

            conn.commit()

            conn.close()

            st.success("Weather data saved to database!")

        else:
            st.warning("City not found!")

    except Exception as e:
        st.warning("An error occurred: " + str(e))
