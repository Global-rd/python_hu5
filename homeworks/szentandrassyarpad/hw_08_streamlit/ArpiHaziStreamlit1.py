import streamlit as st
import pandas as pd
import plotly.express as px
import datetime as dt
import requests
import pprint
from  sqlite_connector import SqliteDb
from pathlib import Path

BASE_LOC_URL = 'https://geocoding-api.open-meteo.com/v1'
BASE_FORECAST_URL='http://api.open-meteo.com/v1/forecast'

@st.cache_data(ttl=86400, show_spinner="Fetching location data ...") # cachelést csinálo dekorator, de nem műxik
def fetch_location_data(city:str) -> dict | None:
    print(f"Fetch data for {city}")
    
    url = f"{BASE_LOC_URL}/search?name={city}&count=1&language=en&format=json"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch data {response.status_code} - {response.text}")

def fetch_weather_data(lat:float, lon:float):
    start_date=dt.date.today()
    end_date = start_date + dt.timedelta(days=5)
    start_date_string = dt.datetime.strftime(start_date, '%Y-%m-%d')
    end_date_string = dt.datetime.strftime(end_date, '%Y-%m-%d')

    
    url=f"{BASE_FORECAST_URL}?latitude={lat}&longitude={lon}&hourly=temperature_2m&current=relative_humidity_2m,temperature_2m,wind_speed_10m&start_date={start_date_string}&end_date={end_date_string}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to weather forecast data {response.status_code} - {response.text}")

def process_forecast_data(weather_data):
    df_temps = pd.DataFrame (weather_data["hourly"])
    ##df_temps["time"]=pd.to_datetime(df_temps["time"])
    df_temps=df_temps.set_index("time")
    df_temps["temperature_2m"]=df_temps["temperature_2m"].astype(float)
    return df_temps

def log(city, weather_data ):
    # A jelenlegi .py fájl könyvtárának lekérése
    BASE_DIR = Path(__file__).resolve().parent
    db_name=st.secrets["weather"]["db_name"] 
    print(f"db_name = {db_name}")

    # Az adatbázis teljes elérési útvonala 
    db_path = BASE_DIR / db_name

    with SqliteDb(db_path) as db:
            
        db.write_single_record("WEATHER_APP_LOG", {
                                                    "CITY":         city, 
                                                    "TEMPERATURE":  weather_data["current"]["temperature_2m"], 
                                                    "HUMIDITY":     weather_data["current"]["relative_humidity_2m"], 
                                                    "WIND_SPEED":   weather_data["current"]["wind_speed_10m"], 
                                                    "LOG_DATE":     dt.datetime.now() 
                                                }
                                )
        df_log = db.select_records("SELECT * FROM WEATHER_APP_LOG ORDER BY LOG_DATE DESC")
        st.write(df_log)
        
def main():
    st.title('Robot Dereams Python - Weather Map & Data Visualization App')
    with st.form("city_form"):
        city = st.text_input(
            "Enter City name: (e.g.: Debrecen)",
            'Debrecen' 
        )
        submitted = st.form_submit_button("Submit")
        print(city)

    if submitted:
        st.session_state.city = city
    
    if "city" not in st.session_state:
        st.session_state.city= 'Debrecen'
    
    location_data = fetch_location_data(st.session_state.city)

    if "results" in location_data:
        
        longitude = location_data['results'][0]['longitude']
        latitude = location_data['results'][0]['latitude']
        country = location_data['results'][0]['country']
        st.header(f'Current Weather in {st.session_state.city}, {country}')

        weather_data = fetch_weather_data(latitude, longitude)
        
        kpi_temperature, kpi_humidity, kpi_windspeed = st.columns(3)
        
        with kpi_temperature:
            st.metric(
                label= f'Temparature ({weather_data["current_units"]["temperature_2m"]})',
                value = f'{weather_data["current"]["temperature_2m"]} {weather_data["current_units"]["temperature_2m"]}'
            )

        with kpi_humidity:
            st.metric(
                label=f'Humidity ({weather_data["current_units"]["relative_humidity_2m"]})',
                value = f'{weather_data["current"]["relative_humidity_2m"]} {weather_data["current_units"]["relative_humidity_2m"]}'
            )

        with kpi_windspeed:
            st.metric(
                label=f'Wind speed ({weather_data["current_units"]["wind_speed_10m"]})',
                value = f'{weather_data["current"]["wind_speed_10m"]} {weather_data["current_units"]["wind_speed_10m"]}'
            )
        df_location=pd.DataFrame(
            {
                "longitude_column": [longitude],
                "latitude_column": [latitude] 
            }
        )

        st.subheader("Weather map")
        st.map(data=df_location, latitude='latitude_column', longitude='longitude_column', zoom=11)

        df_temps = process_forecast_data(weather_data)
        fig_temp = px.line(
                        df_temps,
                        x=df_temps.index,
                        y="temperature_2m", # a df egyik oszlopa
                        labels={"temperature_2m": f"Temperature {weather_data['current_units']['temperature_2m']}"},                        
                        title = "Hourly Temperature Forecast (Next 5 Days)"
                    )
        st.plotly_chart(fig_temp)

        st.subheader("Log")
        log(city, weather_data)
        

    else:
        st.warning(f"No data found for {city}")

if __name__ == "__main__":    
    main()
