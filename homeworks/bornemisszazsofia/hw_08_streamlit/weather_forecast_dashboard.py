import streamlit as st
import plotly.express as px
import pandas as pd
import datetime
import requests

#Basic dashboard layout config:
st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem;
        }

        h1 {
            margin-bottom: 0rem;
        }

        h3 {
            margin-top: 0rem;
        }

        .stVerticalBlock {
            gap: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Current Weather and Forecast")
selected_city_subheader = st.empty()


#Geocoding API GET request:
col1, col2 = st.columns([1,3])
with col1:
    city_input = st.text_input("Please enter a city name.", "Zurich")

geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
geocoding_parameters = {"name": city_input,
                        "count": 10,
                        }

if city_input == "":
    st.stop()
else:
    geocoding_response = requests.get(url=geocoding_url, params=geocoding_parameters).json()
    #print(geocoding_response)

    city_options = []
    if "results" in geocoding_response:
        for city in geocoding_response["results"]:
            #print(f"{city["name"]}, {city["feature_code"]}")
            if city["feature_code"].startswith("PPL") and city["feature_code"] not in ("PPLX", "PPLH", "PPLQ") and city["name"].lower() == city_input.lower():
                city_options.append(city)
        #print((city_options))
        if len(city_options) > 1:
            with col2:
                selected_city = st.selectbox("Select a city:", 
                                        options=city_options,
                                        format_func=lambda city: f"{city["name"]}, {city["admin1"]}, {city["country"]}"
                                        )
        elif len(city_options) == 1:
            selected_city = city_options[0]
        else:
            selected_city = city_options[0]
        
        geocoding_response_latitude = selected_city["latitude"]
        geocoding_response_longitude = selected_city["longitude"]
        #print(f"latitude: {geocoding_response_latitude}, longitude: {geocoding_response_longitude}")
    else:
        st.error(f"No results for {city_input}. Please review your input.")
        st.stop()

#Weather API GET request:
weather_forecast_url = "https://api.open-meteo.com/v1/forecast"
weather_forecast_parameters = {"latitude": geocoding_response_latitude,
                               "longitude": geocoding_response_longitude,
                               "current":["temperature_2m", "relative_humidity_2m", "wind_speed_10m"],
                               "forecast_days": 5,
                               "hourly": "temperature_2m",
                               "timezone": "auto",
                                }
weather_forecast_response = requests.get(url=weather_forecast_url, params=weather_forecast_parameters).json()
#print(weather_forecast_response)

weather_current_temperature = weather_forecast_response["current"]["temperature_2m"]
weather_current_humidity = weather_forecast_response["current"]["relative_humidity_2m"]
weather_current_wind_speed = weather_forecast_response["current"]["wind_speed_10m"]
print(f"Current temperature: {weather_current_temperature} {weather_forecast_response["current_units"]["temperature_2m"]}")
print(f"Current humidity: {weather_current_humidity} {weather_forecast_response["current_units"]["relative_humidity_2m"]}")
print(f"Current wind speed: {weather_current_wind_speed} {weather_forecast_response["current_units"]["wind_speed_10m"]}")

#Weather forecast data into df:
weather_forecast_temperature_df = pd.DataFrame(weather_forecast_response["hourly"], columns= ["time", "temperature_2m"])
#print(weather_forecast_temperature_df)
weather_forecast_temperature_df["time"] = pd.to_datetime(weather_forecast_temperature_df["time"])
#print(weather_forecast_temperature_df.dtypes)

#Weather dashboard:

selected_city_subheader.subheader(f"{selected_city["name"]}, {selected_city["admin1"]}, {selected_city["country"]}")












