import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Weather Dashboard",
    page_icon="🌤️",
    layout="wide"
)

st.title("🌤️ Weather Dashboard")
st.write("Real-time weather data and forecasts for cities around the world.")

city = st.text_input(
    "Enter a city name:",
    value="Budapest"
)

if city.strip():
    try:
        # Step 1: Get city coordinates
        geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

        params = {
            "name": city.strip(),
            "count": 1,
            "language": "en",
            "format": "json"
        }

        response = requests.get(
            geocoding_url,
            params=params,
            timeout=10
        )
        response.raise_for_status()

        data = response.json()

        if "results" in data and data["results"]:
            location = data["results"][0]

            city_name = location["name"]
            country = location["country"]
            latitude = location["latitude"]
            longitude = location["longitude"]

            st.subheader(f"Current Weather in {city_name}, {country}")

            # Step 2: Get weather data
            weather_url = "https://api.open-meteo.com/v1/forecast"

            weather_params = {
                "latitude": latitude,
                "longitude": longitude,
                "current": [
                    "temperature_2m",
                    "relative_humidity_2m",
                    "wind_speed_10m"
                ],
                "daily": [
                    "temperature_2m_max",
                    "temperature_2m_min"
                ],
                "forecast_days": 5,
                "timezone": "auto"
            }

            weather_response = requests.get(
                weather_url,
                params=weather_params,
                timeout=10
            )
            weather_response.raise_for_status()

            weather_data = weather_response.json()
            current = weather_data["current"]

            temperature = current["temperature_2m"]
            humidity = current["relative_humidity_2m"]
            wind_speed = current["wind_speed_10m"]

            # Step 3: Display weather metrics
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    label="🌡️ Temperature",
                    value=f"{temperature} °C"
                )

            with col2:
                st.metric(
                    label="💧 Humidity",
                    value=f"{humidity}%"
                )

            with col3:
                st.metric(
                    label="💨 Wind Speed",
                    value=f"{wind_speed} km/h"
                )

            # Step 4: Display city on a map
            st.subheader("📍 City Location")

            map_data = pd.DataFrame({
                "lat": [latitude],
                "lon": [longitude]
            })

            st.map(map_data)

            # Step 5: Five-day weather forecast
            st.subheader("📈 5-Day Temperature Forecast")

            daily = weather_data["daily"]

            forecast_df = pd.DataFrame({
                "Date": pd.to_datetime(daily["time"]),
                "Max Temperature": daily["temperature_2m_max"],
                "Min Temperature": daily["temperature_2m_min"]
            })

            forecast_df = forecast_df.set_index("Date")

            st.line_chart(
                forecast_df,
                y=["Max Temperature", "Min Temperature"],
                y_label="Temperature (°C)"
            )

            # Step 6: Display forecast table
            st.subheader("📋 Forecast Data")

            st.dataframe(
                forecast_df,
                use_container_width=True
            )

        else:
            st.warning("City not found. Please try another city.")

    except requests.RequestException as error:
        st.warning(f"Unable to retrieve weather data: {error}")

    except (KeyError, IndexError, TypeError, ValueError):
        st.warning("Unexpected data received from the weather API.")

else:
    st.warning("Please enter a city name.")
