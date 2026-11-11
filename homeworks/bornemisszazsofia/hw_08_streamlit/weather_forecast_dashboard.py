import streamlit as st
import plotly.express as px
import pandas as pd
import datetime
import requests
import sqlite3
from pathlib import Path


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
search_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


#Geocoding API GET request:
col1, col2, col3 = st.columns([1,3,2])
with col1:
    city_input = st.text_input("Please enter a city name.", "Zurich")

geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
geocoding_parameters = {"name": city_input,
                        "count": 10,
                        }

if city_input == "":
    st.stop()
else:
    try:
        geocoding_request = requests.get(url=geocoding_url, params=geocoding_parameters, timeout=10)
        if geocoding_request.status_code != 200:
            st.error(f"API request failed. Error code: {geocoding_request.status_code}")
            st.stop()
        geocoding_response = geocoding_request.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
        st.stop()

    city_options = []
    if "results" in geocoding_response:
        for city in geocoding_response["results"]:
            if city["feature_code"].startswith("PPL") and city["feature_code"] not in ("PPLX", "PPLH", "PPLQ") and city["name"].lower() == city_input.lower():
                city_options.append(city)
        if len(city_options) > 1:
            with col2:
                selected_city = st.selectbox("Select a city:", 
                                        options=city_options,
                                        format_func=lambda city: f"{city["name"]}, {city.get('admin1', ' ')}, {city.get('country', ' ')}"
                                        )
        elif len(city_options) == 1:
            selected_city = city_options[0]
        else:
            st.error(f"No matching city found for {city_input}.")
            st.stop()
        geocoding_response_latitude = selected_city["latitude"]
        geocoding_response_longitude = selected_city["longitude"]
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
try:
    weather_forecast_request = requests.get(url=weather_forecast_url, params=weather_forecast_parameters, timeout=10)
    if weather_forecast_request.status_code != 200:
        st.error(f"API request failed. Error code: {weather_forecast_request.status_code}")
        st.stop()    
    weather_forecast_response = weather_forecast_request.json()
except requests.exceptions.RequestException as e:
    st.error(f"Request failed: {e}")
    st.stop()

#Current weather data:
weather_current_temperature = weather_forecast_response["current"]["temperature_2m"]
weather_current_humidity = weather_forecast_response["current"]["relative_humidity_2m"]
weather_current_wind_speed = weather_forecast_response["current"]["wind_speed_10m"]

#Weather forecast data into df:
weather_forecast_temperature_df = pd.DataFrame(weather_forecast_response["hourly"], columns= ["time", "temperature_2m"])
weather_forecast_temperature_df["time"] = pd.to_datetime(weather_forecast_temperature_df["time"])


#Weather dashboard:
selected_city_subheader.subheader(f"{selected_city["name"]}, {selected_city.get("admin1", ' ')}, {selected_city.get("country", ' ')}")
kpi_current_temperature, kpi_current_humidity, kpi_current_wind_speed, col4 = st.columns([1,1,1,3])

if weather_current_temperature is not None and weather_current_humidity is not None and weather_current_wind_speed is not None:
    with kpi_current_temperature:
        st.metric(label="Temperature",
                value=f"{weather_current_temperature} {weather_forecast_response["current_units"]["temperature_2m"]}"
                )
    with kpi_current_humidity:
        st.metric(label="Humidity",
                value=f"{weather_current_humidity} {weather_forecast_response["current_units"]["relative_humidity_2m"]}"
                )
    with kpi_current_wind_speed:
        st.metric(label="Wind Speed",
                value=f"{weather_current_wind_speed} {weather_forecast_response["current_units"]["wind_speed_10m"]}"
                )  
missing_weather_data = []
if weather_current_temperature is None:
    missing_weather_data.append("Temperature")
if weather_current_humidity is None:
    missing_weather_data.append("Humidity")
if weather_current_wind_speed is None:
    missing_weather_data.append("Wind speed")              
if missing_weather_data:
    st.error(f"No {missing_weather_data} data found for {selected_city}.")


#Map chart:
current_weather_df = pd.DataFrame([{"latitude": geocoding_response_latitude, "longitude": geocoding_response_longitude}])
col1, col2 = st.columns([2,3])
with col1:
    st.header("Location Map")
    weather_map_chart = st.map(current_weather_df,
                            latitude= "latitude",
                            longitude= "longitude",
                            width="stretch",
                            height=400,
                            zoom=4,
                            color= "#00FF0D",
                            size=None,
                            )

#Line chart for forecast:
y_min = (weather_forecast_temperature_df["temperature_2m"].min() // 5) * 5 - 5
y_max = (weather_forecast_temperature_df["temperature_2m"].max() // 5) * 5 + 10
with col2:
    st.header("Hourly Temperature Forecast (next 5 days, in °C)")
    weather_forecast_chart = px.line(weather_forecast_temperature_df,
                                    x="time",
                                    y="temperature_2m",
                                    )
    
    weather_forecast_chart.update_layout(yaxis_title="",
                                        yaxis_range=[y_min, y_max],
                                        yaxis_dtick= 5,
                                        xaxis_title="",
                                        xaxis_dtick=14400000,
                                        xaxis_tickformat="%d.%m %H:%M",
                                        xaxis_tickangle=-90,
                                        height=400,
                                        )
    weather_forecast_chart.update_traces(line_color="#00FF0D")
    st.plotly_chart(weather_forecast_chart)


#Records for searches:
record = {"search_time":search_time, 
          "city": selected_city["name"],
          "temperature": weather_current_temperature,
          "humidity": weather_current_humidity,
          "wind_speed": weather_current_wind_speed
          }
db_path = Path(__file__).parent / "weather_records.db"

class WeatherSearchRecords:


    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            return self
        except Exception as open_error:
            raise RuntimeError(f"Failed to open database {self.db_name}") from open_error

    def __exit__(self, *args):
        if self.conn:
            try:
                self.conn.close()
            except Exception as close_error:
                print(f"Error: failed to close connection to {self.db_name}: {close_error}")

    def create_table(self):
        self.conn.execute("""CREATE TABLE IF NOT EXISTS weather_searches
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            search_time TEXT,
                            city TEXT, 
                            temperature REAL,
                            humidity REAL,
                            wind_speed REAL
                            )
                        """)
    
    def write_single_record(self, record):
       
        query = """INSERT INTO weather_searches 
        (search_time, city, temperature, humidity, wind_speed) 
        VALUES (?, ?, ?, ?, ?)"""
        with self.conn:
            self.conn.execute(query, tuple(record.values()))

    def select_records(self, query):
        weather_records_df = pd.read_sql(query, self.conn)
        return weather_records_df

with WeatherSearchRecords(db_path) as db:
    db.create_table()

    if "last_search" not in st.session_state:
        st.session_state.last_search = None

    if st.session_state.last_search != selected_city["id"]:
        db.write_single_record(record)
        st.session_state.last_search = selected_city["id"]
    
    weather_records_df_result = db.select_records("SELECT * FROM weather_searches")
    print(weather_records_df_result)

    








